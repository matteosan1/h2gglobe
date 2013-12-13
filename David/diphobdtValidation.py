import ROOT
import sys
import array
import math
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d","--drawPlot",    default=False, help="Draw plots. \nDefault: %default", action="store_true")
parser.add_option("-b","--blinding",    default=False, help="Draw blinded plots. \nDefault: %default", action="store_true")
parser.add_option("-t","--transform",   default=False, help="Transform BDT output to have flat signal. \nDefault: %default", action="store_true")
parser.add_option("-l","--eventLooper", default=False, help="Loop on the events. \nDefault: %default", action="store_true")
parser.add_option("-i","--inFile",      default="opttree_8TeV_v2.root", help="Input file to be read. \nDefault: %default")
parser.add_option("-o","--outFile",     default="output.root", help="Output file to be produced. \nDefault: %default")
parser.add_option("-7","--TeV",         default=8, help="Number of photon categories for globe smearing. \nDefault: %default", type=int)
parser.add_option("-z","--Z",           default=False, help="Zee control plots. \nDefault: %default", action="store_true")
(options,arg) = parser.parse_args()

ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptStat(0)
#ROOT.gROOT.SetBatch(0)

transformations = []
hBDTOutput = []
hBDTIDUpOutput = []
hBDTIDDownOutput = []
hBDTSigmaUpOutput = []
hBDTSigmaDownOutput = []
hDijetOutput = []
hCombinedOutput = []
groupType = []
bdtCategories = []
combinedCategories = []
colors = []
kfactors = []

def variableBinning(hnew, hold, bins):
    nold = hold.GetXaxis().GetNbins()
    e = [0 for i in xrange(len(bins))]
    for i in xrange(hold.GetXaxis().GetNbins()):
        eold = hold.GetBinError(i)
        j = hnew.Fill(hold.GetXaxis().GetBinCenter(i), hold.GetBinContent(i)) 
        e[j] += eold*eold; 
        
    for j in xrange(len(bins)):
        hnew.SetBinError(j, math.sqrt(e[j])) 
    
    return hnew

def transformX(hTot, h, eff):
    q = array.array('d', [0, 0])
    probSum = array.array('d', [eff, eff+0.01])
    hTot.GetQuantiles(len(probSum), q, probSum)
    bin1 = h.FindBin(q[0])
    bin2 = h.FindBin(q[1])
    intError = array.array('d', [0])
    integral = h.IntegralAndError(bin1, bin2, intError)
    #print 1-eff, 1- eff+0.01, integral, intError[0], q[0] - q[1]
    return (integral, intError[0])#/math.sqrt(float(h.GetEntries())/float(h.Integral())))

def readHistos(f):
    for i in xrange(16):
        hBDTOutput.append(f.Get("hBDTOutput"+str(i)))
        hBDTIDUpOutput.append(f.Get("hBDTIDUpOutput"+str(i)))
        hBDTIDDownOutput.append(f.Get("hBDTIDDownOutput"+str(i)))
        hBDTSigmaUpOutput.append(f.Get("hBDTSigmaUpOutput"+str(i)))
        hBDTSigmaDownOutput.append(f.Get("hBDTSigmaDownOutput"+str(i)))
        hDijetOutput.append(f.Get("hDijetOutput"+str(i)))
        hCombinedOutput.append(f.Get("hCombinedOutput"+str(i)))

def checkBDTCat(bdt, cats):
    for i in xrange(len(cats)-1):
        if (bdt > cats[i] and bdt <cats[i+1]):
            return len(cats)-2-i
    return -1

def checkCiCCat(eta1, r91, eta2, r92):
    if ((abs(eta1) < 1.479 and abs(eta2) < 1.479) and (r91>0.94 and r92>0.94)):
        return 0
    if ((abs(eta1) < 1.479 and abs(eta2) < 1.479) and not (r91>0.94 and r92 > 0.94)):
        return 1
    if (not (abs(eta1) < 1.479 and abs(eta2) < 1.479) and (r91>0.94 and r92 > 0.94)):
        return 2
    if (not (abs(eta1) < 1.479 and abs(eta2) < 1.479) and not (r91>0.94 and r92 > 0.94)):
        return 3

def checkSampleCat(samples, s):
    for i, c in enumerate(samples):
        if (s in c):
            return i, c.index(s)   
    return -1, -1

def eventLoop():
    for i in xrange(16):
        hBDTOutput.append(ROOT.TH1F("hBDTOutput"+str(i), "hBDTOutput"+str(i), 500, -1, 1))
        hBDTIDUpOutput.append(ROOT.TH1F("hBDTIDUpOutput"+str(i), "hBDTIDUpOutput"+str(i), 500, -1, 1))
        hBDTIDDownOutput.append(ROOT.TH1F("hBDTIDDownOutput"+str(i), "hBDTIDDownOutput"+str(i), 500, -1, 1))
        hBDTSigmaUpOutput.append(ROOT.TH1F("hBDTSigmaUpOutput"+str(i), "hBDTSigmaUpOutput"+str(i), 500, -1, 1))
        hBDTSigmaDownOutput.append(ROOT.TH1F("hBDTSigmaDownOutput"+str(i), "hBDTSigmaDownOutput"+str(i), 500, -1, 1))
        hDijetOutput.append(ROOT.TH1F("hDijetOutput"+str(i), "hDijetOutput"+str(i), 500, -1, 1))
        hCombinedOutput.append(ROOT.TH1F("hCombinedOutput"+str(i), "hCombinedOutput"+str(i), 500, -1, 1))

    infile = ROOT.TFile(options.inFile)
    tree = infile.Get("opttree")

    entries = tree.GetEntries()
    print "File entries: ", entries
    for z in xrange(entries):
        tree.GetEntry(z)
    
        if (z%100000 == 0):
            print z

        if (tree.ptoM1<0.33 or tree.ptoM2<0.25):
            continue
            
        if (tree.idmva1<-0.2 or tree.idmva2<-0.2):
            continue

        if (tree.mass<130 and tree.mass >120 and options.blinding):
            continue
        weight = tree.full_weight
        # hack for Sherpa 8 TeV
        if (tree.itype == 3):
            weight = weight*0.85
        if (options.TeV != 7 and (tree.itype == 11 or tree.itype == 21)):
            weight = weight/1.3

        # hack for 7TeV ntuple
        dijet = -1#tree.bdt_dijet
        comb = -1#tree.bdt_combined_dijet
        if (not options.Z):
            if (options.TeV == 7):
                dijet = tree.bdt_dijet_7TeV_ptrewght
                comb = tree.bdt_combined_dijet7TeV_ptrewght
            else:
                dijet = tree.bdt_dijet
                comb = tree.bdt_combined_dijet

        if (tree.itype == 0):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                if (options.transform):
                    hDijetOutput[0].Fill(transformations[1].Eval(dijet), weight)
                    hCombinedOutput[0].Fill(comb, weight)
                else:
                    hDijetOutput[0].Fill(dijet, weight)
                    hCombinedOutput[0].Fill(comb, weight)
            #else:
            if (options.transform):
                hBDTOutput[0].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                if (abs(tree.eta1) < 1.479 and abs(tree.eta2)<1.479):
                    hBDTOutput[13].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                elif (abs(tree.eta1) > 1.479 and abs(tree.eta2)>1.479):
                    hBDTOutput[15].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                else:
                    hBDTOutput[14].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[0].Fill(tree.dipho_mva, weight)
                if (abs(tree.eta1) < 1.479 and abs(tree.eta2)<1.479):
                    hBDTOutput[10].Fill(tree.dipho_mva, weight)
                elif (abs(tree.eta1) > 1.479 and abs(tree.eta2)>1.479):
                    hBDTOutput[12].Fill(tree.dipho_mva, weight)
                else:
                    hBDTOutput[11].Fill(tree.dipho_mva, weight)
        elif (tree.itype > 0):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                if (options.transform):
                    hDijetOutput[1].Fill(transformations[1].Eval(dijet), weight)
                    hCombinedOutput[1].Fill(comb, weight)
                else:
                    hDijetOutput[1].Fill(dijet, weight)
                    hCombinedOutput[1].Fill(comb, weight)
            #else:
            if (options.transform):
                hBDTOutput[1].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[1].Fill(tree.dipho_mva, weight)
                #hBDTIDUpOutput[1].Fill(tree.dipho_mva_idu, weight)
                #hBDTIDDownOutput[1].Fill(tree.dipho_mva_idd, weight)
                #hBDTSigmaUpOutput[1].Fill(tree.dipho_mva_sEu, weight)
                #hBDTSigmaDownOutput[1].Fill(tree.dipho_mva_sEd, weight)

            sampleCat, typeInd = checkSampleCat(groupType, tree.itype)
            if (sampleCat > 0 and sampleCat < 4):
                if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                    if (options.transform):
                        hDijetOutput[5+sampleCat].Fill(transformations[1].Eval(dijet), weight)
                        hCombinedOutput[5+sampleCat].Fill(comb, weight)
                    else:
                        hDijetOutput[5+sampleCat].Fill(dijet, weight)
                        hCombinedOutput[5+sampleCat].Fill(comb, weight)
                #else:
                if (options.transform):
                    hBDTOutput[5+sampleCat].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                else:
                    hBDTOutput[5+sampleCat].Fill(tree.dipho_mva, weight)
                    #hBDTIDUpOutput[5+sampleCat].Fill(tree.dipho_mva_idu, weight)
                    #hBDTIDDownOutput[5+sampleCat].Fill(tree.dipho_mva_idd, weight)
                    #hBDTSigmaUpOutput[5+sampleCat].Fill(tree.dipho_mva_sEu, weight)
                    #hBDTSigmaDownOutput[5+sampleCat].Fill(tree.dipho_mva_sEd, weight)

        elif (tree.itype == -125000):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                if (options.transform):
                    hDijetOutput[2].Fill(transformations[1].Eval(dijet), weight)
                    hCombinedOutput[2].Fill(comb, weight)
                else:
                    hDijetOutput[2].Fill(dijet, weight)
                    hCombinedOutput[2].Fill(comb, weight)
            #else:
            if (options.transform):
                hBDTOutput[2].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[2].Fill(tree.dipho_mva, weight)
                #hBDTIDUpOutput[2].Fill(tree.dipho_mva_idu, weight)
                #hBDTIDDownOutput[2].Fill(tree.dipho_mva_idd, weight)
                #hBDTSigmaUpOutput[2].Fill(tree.dipho_mva_sEu, weight)
                #hBDTSigmaDownOutput[2].Fill(tree.dipho_mva_sEd, weight)

        elif (tree.itype == -38):
            if (options.transform):
                hBDTOutput[9].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                if (abs(tree.eta1) < 1.479 and abs(tree.eta2)<1.479):
                    hBDTOutput[10].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                elif (abs(tree.eta1) > 1.479 and abs(tree.eta2)>1.479):
                    hBDTOutput[12].Fill(transformations[0].Eval(tree.dipho_mva), weight)
                else:
                    hBDTOutput[11].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[9].Fill(tree.dipho_mva, weight)
                if (abs(tree.eta1) < 1.479 and abs(tree.eta2)<1.479):
                    hBDTOutput[10].Fill(tree.dipho_mva, weight)
                elif (abs(tree.eta1) > 1.479 and abs(tree.eta2)>1.479):
                    hBDTOutput[12].Fill(tree.dipho_mva, weight)
                else:
                    hBDTOutput[11].Fill(tree.dipho_mva, weight)

        elif (tree.itype == -125100):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                if (options.transform):
                    hDijetOutput[3].Fill(transformations[1].Eval(dijet), weight)
                    hCombinedOutput[3].Fill(comb, weight)
                else:
                    hDijetOutput[3].Fill(dijet, weight)
                    hCombinedOutput[3].Fill(comb, weight)
            #else:
            if (options.transform):
                hBDTOutput[3].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[3].Fill(tree.dipho_mva, weight)
                #hBDTIDUpOutput[3].Fill(tree.dipho_mva_idu, weight)
                #hBDTIDDownOutput[3].Fill(tree.dipho_mva_idd, weight)
                #hBDTSigmaUpOutput[3].Fill(tree.dipho_mva_sEu, weight)
                #hBDTSigmaDownOutput[3].Fill(tree.dipho_mva_sEd, weight)

        elif (tree.itype == -125400):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                if (options.transform):
                    hDijetOutput[4].Fill(transformations[1].Eval(dijet), weight)
                    hCombinedOutput[4].Fill(comb, weight)
                else:
                    hDijetOutput[4].Fill(dijet, weight)
                    hCombinedOutput[4].Fill(comb, weight)
            #else:
            if (options.transform):
                hBDTOutput[4].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[4].Fill(tree.dipho_mva, weight)
                #hBDTIDUpOutput[4].Fill(tree.dipho_mva_idu, weight)
                #hBDTIDDownOutput[4].Fill(tree.dipho_mva_idd, weight)
                #hBDTSigmaUpOutput[4].Fill(tree.dipho_mva_sEu, weight)
                #hBDTSigmaDownOutput[4].Fill(tree.dipho_mva_sEd, weight)

        elif (tree.itype == -125500):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                if (options.transform):
                    hDijetOutput[5].Fill(transformations[1].Eval(dijet), weight)
                    hCombinedOutput[5].Fill(comb, weight)
                else:
                    hDijetOutput[5].Fill(dijet, weight)
                    hCombinedOutput[5].Fill(comb, weight)
            #else:
            if (options.transform):
                hBDTOutput[5].Fill(transformations[0].Eval(tree.dipho_mva), weight)
            else:
                hBDTOutput[5].Fill(tree.dipho_mva, weight)
                #hBDTIDUpOutput[5].Fill(tree.dipho_mva_idu, weight)
                #hBDTIDDownOutput[5].Fill(tree.dipho_mva_idd, weight)
                #hBDTSigmaUpOutput[5].Fill(tree.dipho_mva_sEu, weight)
                #hBDTSigmaDownOutput[5].Fill(tree.dipho_mva_sEd, weight)

    all_histos = hBDTOutput + hDijetOutput + hCombinedOutput + hBDTIDUpOutput + hBDTIDDownOutput + hBDTSigmaUpOutput + hBDTSigmaDownOutput
    output = ROOT.TFile(options.outFile, "recreate")
    for h in all_histos:
        h.Write()
    output.Close()

def errors(hU, hD, r):
    meanUp = hU[r[0]].Clone()
    meanDown = hD[r[0]].Clone()
    for i in r[1:]:
        meanUp.Add(hU[i])
        meanDown.Add(hD[i])
    mean = meanUp.Clone()
    mean.Add(meanDown)
    mean.Scale(0.5)
    for i in xrange(1, mean.GetXaxis().GetNbins()+1):
        up = meanUp.GetBinContent(i)
        down = meanDown.GetBinContent(i)
        mean.SetBinError(i, (up-down)/2.)

    return mean, meanUp, meanDown

def drawPlots():
    inputFile = ROOT.TFile(options.inFile)
    readHistos(inputFile)

    if (options.Z):
        c3 = ROOT.TCanvas("c3", "c3", 1600, 800)
        c3.Divide(4, 2)
        plotIndexMC   = [9, 10, 11, 12]
        plotIndexData = [0, 13, 14, 15]
        labels = ["BDT Classifier (All)","BDT Classifier (EB-EB)","BDT Classifier (EB-EE)","BDT Classifier (EE-EE)"]
        l3 = []
        temp1 = []
        temp2 = []
        for nC in xrange(4):
            c3.GetPad(nC+1).SetPad(0.005+(nC*0.25), 0.25, 0.255+(nC*0.25), .995)
            c3.cd(nC+1) 
            #c3.GetPad(nC+1).SetLogy(1)
            hBDTOutput[plotIndexMC[nC]].SetFillColor(38)
            hBDTOutput[plotIndexMC[nC]].Rebin(10)
            hBDTOutput[plotIndexData[nC]].Rebin(10)
            hBDTOutput[plotIndexMC[nC]].Scale(hBDTOutput[plotIndexData[nC]].Integral()/hBDTOutput[plotIndexMC[nC]].Integral())
            hBDTOutput[plotIndexMC[nC]].Draw()
            hBDTOutput[plotIndexMC[nC]].SetMaximum(hBDTOutput[plotIndexMC[nC]].GetMaximum()*1.5)
            hBDTOutput[plotIndexData[nC]].SetMarkerStyle(20)
            hBDTOutput[plotIndexData[nC]].Draw("PESAME")
            hBDTOutput[plotIndexMC[nC]].GetXaxis().SetTitle(labels[nC])
            hBDTOutput[plotIndexMC[nC]].GetYaxis().SetTitle("# of events/0.04")
            hBDTOutput[plotIndexMC[nC]].GetYaxis().SetTitleOffset(1.2)
            txt1 = ROOT.TLatex()
            txt1.SetNDC()
            txt1.SetTextSize(0.05)
            txt1.SetTextAlign(12)
            if (options.TeV == 8):
                txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
                l3.append(ROOT.TLegend(0.45, 0.65, 0.88, 0.80))
            else:
                txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
                l3.append(ROOT.TLegend(0.45, 0.65, 0.88, 0.80))
            l3[-1].SetFillColor(ROOT.kWhite)
            l3[-1].SetBorderSize(0)
            l3[-1].AddEntry(hBDTOutput[0], "Data", "PE")
            l3[-1].AddEntry(hBDTOutput[9], "DYJets", "F")
            l3[-1].Draw("SAME")    
            c3.cd(nC+5)
            c3.GetPad(nC+5).SetPad(0.005+(nC*0.25), 0.005, 0.255+(nC*0.25), .25)
            temp2.append(hBDTOutput[plotIndexData[nC]].Clone())
            temp1.append(hBDTOutput[plotIndexMC[nC]].Clone())
            temp2[-1].Sumw2()
            temp2[-1].Divide(temp1[-1])
            temp2[-1].Draw("PE")
            temp2[-1].GetYaxis().SetRangeUser(0., 2.0)
            temp2[-1].SetLineColor(ROOT.kBlue)
            temp2[-1].SetMarkerColor(ROOT.kBlue)
            temp2[-1].SetMarkerStyle(20)
            c3.GetPad(nC+5).SetGridx(1)
            c3.GetPad(nC+5).SetGridy(1)
        c3.SaveAs("diphobdt_zee.png")
    else:
        # DIPHO BDT SIGNAL
        c2 = ROOT.TCanvas("c2", "c2")
        stackBDTSignal = ROOT.THStack("s2", "s2")
        hBDTOutput[2].SetFillColor(ROOT.kRed)
        hBDTOutput[3].SetFillColor(ROOT.kYellow)
        hBDTOutput[5].SetFillColor(ROOT.kGreen)
        hBDTOutput[4].SetFillColor(ROOT.kBlue)
        hBDTOutput[2].Rebin(10)
        hBDTOutput[3].Rebin(10)
        hBDTOutput[4].Rebin(10)
        hBDTOutput[5].Rebin(10)
        stackBDTSignal.Add(hBDTOutput[4])
        stackBDTSignal.Add(hBDTOutput[5])
        stackBDTSignal.Add(hBDTOutput[3])
        stackBDTSignal.Add(hBDTOutput[2])
        stackBDTSignal.Draw()
        #mean.Draw("E2SAME")
        #mean.SetFillColor(ROOT.kBlue)
        #mean.SetFillStyle(3001)
        #mean.SetMarkerStyle(0)
        if (options.TeV == 8):
            stackBDTSignal.SetMaximum(25)
        else:
            if (options.transform):
                stackBDTSignal.SetMaximum(5)
    
        stackBDTSignal.GetXaxis().SetTitle("BDT Classifier")
        stackBDTSignal.GetYaxis().SetTitle("# of events/0.04")
        stackBDTSignal.GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        l2 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.65, 0.60, 0.80)
        else:
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.65, 0.60, 0.80)
        l2.SetFillColor(ROOT.kWhite)
        l2.SetBorderSize(0)
        l2.AddEntry(hBDTOutput[2], "GF (m_{H}=125 GeV)", "F")
        l2.AddEntry(hBDTOutput[3], "VBF", "F")
        l2.AddEntry(hBDTOutput[5], "WH/ZH", "F")
        l2.AddEntry(hBDTOutput[4], "ttH", "F")
        l2.Draw("SAME")
        if (not options.transform):
            lines = []
            for i in bdtCategories[0:-1]:
                lines.append(ROOT.TLine(i, 0, i, stackBDTSignal.GetMaximum()*0.8))
                lines[-1].Draw("SAME")
        c2.SaveAs("diphobdt_signal.png")
        c2.SaveAs("diphobdt_signal.pdf")
    
        c13 = ROOT.TCanvas("c13", "c13")
        #c2.Divide(2, 1)
        #c2.cd(1)
        stackCombinedSignal = ROOT.THStack("s13", "s13")
        hCombinedOutput[2].SetFillColor(ROOT.kRed)
        hCombinedOutput[3].SetFillColor(ROOT.kYellow)
        hCombinedOutput[5].SetFillColor(ROOT.kGreen)
        hCombinedOutput[4].SetFillColor(ROOT.kBlue)
        hCombinedOutput[2].Rebin(10)
        hCombinedOutput[3].Rebin(10)
        hCombinedOutput[4].Rebin(10)
        hCombinedOutput[5].Rebin(10)
        stackCombinedSignal.Add(hCombinedOutput[4])
        stackCombinedSignal.Add(hCombinedOutput[5])
        stackCombinedSignal.Add(hCombinedOutput[3])
        stackCombinedSignal.Add(hCombinedOutput[2])
        stackCombinedSignal.Draw()
        if (options.TeV == 8):
            stackCombinedSignal.SetMaximum(5)
        else:
            c13.SetLogy()
        stackCombinedSignal.GetXaxis().SetTitle("BDT Classifier")
        stackCombinedSignal.GetYaxis().SetTitle("# of events/0.04")
        stackCombinedSignal.GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (not options.transform):
            lines = []
            for i in combinedCategories[0:-1]:
                lines.append(ROOT.TLine(i, 0, i, stackCombinedSignal.GetMaximum()*0.8))
                lines[-1].Draw("SAME")
        l2 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.65, 0.60, 0.80)
        else:
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.65, 0.60, 0.80)
        l2.SetFillColor(ROOT.kWhite)
        l2.SetBorderSize(0)
        l2.AddEntry(hCombinedOutput[2], "GF (m_{H}=125 GeV)", "F")
        l2.AddEntry(hCombinedOutput[3], "VBF", "F")
        l2.AddEntry(hCombinedOutput[5], "WH/ZH", "F")
        l2.AddEntry(hCombinedOutput[4], "ttH", "F")
        l2.Draw("SAME")
        c13.SaveAs("combinedbdt_signal.png")
        c13.SaveAs("combinedbdt_signal.pdf")
    
        c12 = ROOT.TCanvas("c12", "c12")
        #c2.Divide(2, 1)
        #c2.cd(1)
        stackDijetSignal = ROOT.THStack("s12", "s12")
        hDijetOutput[2].SetFillColor(ROOT.kRed)
        hDijetOutput[3].SetFillColor(ROOT.kYellow)
        hDijetOutput[5].SetFillColor(ROOT.kGreen)
        hDijetOutput[4].SetFillColor(ROOT.kBlue)
        for z in [2,3,4,5]:
            hDijetOutput[z].Rebin(20)
        stackDijetSignal.Add(hDijetOutput[4])
        stackDijetSignal.Add(hDijetOutput[5])
        stackDijetSignal.Add(hDijetOutput[3])
        stackDijetSignal.Add(hDijetOutput[2])
        stackDijetSignal.Draw()
        if (options.TeV == 8):
            if (not options.transform):
                stackDijetSignal.SetMaximum(3)
            else:
                stackDijetSignal.SetMaximum(4)
        stackDijetSignal.GetXaxis().SetTitle("BDT Classifier")
        stackDijetSignal.GetYaxis().SetTitle("# of events/0.04")
        stackDijetSignal.GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        l2 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.65, 0.60, 0.80)
        else:
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.65, 0.60, 0.80)
        l2.SetFillColor(ROOT.kWhite)
        l2.SetBorderSize(0)
        l2.AddEntry(hDijetOutput[2], "GF (m_{H}=125 GeV)", "F")
        l2.AddEntry(hDijetOutput[3], "VBF", "F")
        l2.AddEntry(hDijetOutput[5], "WH/ZH", "F")
        l2.AddEntry(hDijetOutput[4], "ttH", "F")
        l2.Draw("SAME")
        c12.SaveAs("dijetbdt_signal.png")
        c12.SaveAs("dijetbdt_signal.pdf")
    
        c3 = ROOT.TCanvas("c3", "c3", 800, 800)
        c3.Divide(1, 2)
        c3.cd(1) 
        c3.GetPad(1).SetPad(0.005, 0.25, 0.995, .995)
        #c3.GetPad(1).SetLogy(1)
        stackBDTBg = ROOT.THStack("s3", "s3")
        hBDTOutput[6].SetFillColor(ROOT.kGreen)
        hBDTOutput[7].SetFillColor(ROOT.kYellow)
        hBDTOutput[8].SetFillColor(ROOT.kRed)
        hBDTOutput[0].Rebin(10)
        hBDTOutput[6].Rebin(10)
        hBDTOutput[7].Rebin(10)
        hBDTOutput[8].Rebin(10)
        stackBDTBg.Add(hBDTOutput[6])
        stackBDTBg.Add(hBDTOutput[7])
        stackBDTBg.Add(hBDTOutput[8])
        stackBDTBg.Draw()
        if (options.TeV == 7):
            if (not options.transform):
                stackBDTBg.SetMaximum(25000)
            else:
                stackBDTBg.SetMaximum(50000)
        else:
            stackBDTBg.SetMaximum(200000)
        hBDTOutput[0].SetMarkerStyle(20)
        #hBDTOutput[0].SetMarkerSize(0.5)
        hBDTOutput[0].Draw("PESAME")
        stackBDTBg.GetXaxis().SetTitle("BDT Classifier")
        stackBDTBg.GetYaxis().SetTitle("# of events/0.04")
        stackBDTBg.GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (not options.transform):
            lines = []
            for i in bdtCategories[0:-1]:
                lines.append(ROOT.TLine(i, 0, i, stackBDTBg.GetMaximum()*0.5))
                lines[-1].Draw("SAME")
        l3 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l3 = ROOT.TLegend(0.45, 0.55, 0.88, 0.80)
        else:
            txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l3 = ROOT.TLegend(0.45, 0.55, 0.88, 0.80)
        l3.SetFillColor(ROOT.kWhite)
        l3.SetBorderSize(0)
        l3.AddEntry(hBDTOutput[0], "Data", "PE")
        l3.AddEntry(hBDTOutput[8], "Fake-Fake", "F")
        l3.AddEntry(hBDTOutput[7], "Prompt-Fake", "F")
        l3.AddEntry(hBDTOutput[6], "Prompt-Prompt", "F")
        l3.Draw("SAME")
    
        c3.cd(2)
        c3.GetPad(2).SetPad(0.005, 0.005, 0.995, .25)
        temp2 = hBDTOutput[0].Clone()
        temp1 = hBDTOutput[8].Clone()
        temp2.Sumw2()
        temp1.Add(hBDTOutput[7])
        temp1.Add(hBDTOutput[6])
        temp2.Divide(temp1)
        temp2.Draw("PE")
        temp2.GetYaxis().SetRangeUser(0., 2.0)
        temp2.SetLineColor(ROOT.kBlue)
        temp2.SetMarkerColor(ROOT.kBlue)
        temp2.SetMarkerStyle(20)
        c3.GetPad(2).SetGridx(1)
        c3.GetPad(2).SetGridy(1)
        c3.SaveAs("diphobdt_bg.png")
        c3.SaveAs("diphobdt_bg.pdf")
        
        c5 = ROOT.TCanvas("c5", "c5", 800, 800)
        c5.Divide(1, 2)
        c5.cd(1)
        c5.GetPad(1).SetPad(0.005, 0.25, 0.995, .995)
        #c5.GetPad(1).SetLogy(1)
        stackDijetBg = ROOT.THStack("s5", "s5")
        hNBDijetOutput = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if (options.transform):
            #if (options.TeV == 8):
            bins = array.array('f', [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
            #bins = array.array('f', [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
            for z in [6,7,8,0]:
                hNBDijetOutput[z] = variableBinning(ROOT.TH1F("hNBDijetOutput"+str(z), "hNBDijetOutput"+str(z), len(bins)-1, bins), hDijetOutput[z], bins)
        else:
            for z in [6,7,8,0]:
                hNBDijetOutput[z] = hDijetOutput[z]
                hDijetOutput[z].Rebin(10)

        hNBDijetOutput[6].SetFillColor(ROOT.kGreen)
        hNBDijetOutput[7].SetFillColor(ROOT.kYellow)
        hNBDijetOutput[8].SetFillColor(ROOT.kRed)
        stackDijetBg.Add(hNBDijetOutput[6])
        stackDijetBg.Add(hNBDijetOutput[7])
        stackDijetBg.Add(hNBDijetOutput[8])
        stackDijetBg.Draw("HIST")
        if (options.TeV == 7):
            if (not options.transform):
                stackDijetBg.SetMaximum(300)
            else:
                stackDijetBg.SetMaximum(2000)
        else:
            if (not options.transform):
                stackDijetBg.SetMaximum(150)
            else:
                stackDijetBg.SetMaximum(8000)
    
        hNBDijetOutput[0].SetMarkerStyle(20)
        hNBDijetOutput[0].Draw("PESAME")
        stackDijetBg.GetXaxis().SetTitle("BDT Classifier")
        stackDijetBg.GetYaxis().SetTitle("# of events/0.04")
        stackDijetBg.GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        l5 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l5 = ROOT.TLegend(0.45, 0.55, 0.88, 0.80)
        else:
            txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l5 = ROOT.TLegend(0.45, 0.55, 0.85, 0.80)
        l5.SetFillColor(ROOT.kWhite)
        l5.SetBorderSize(0)
        l5.AddEntry(hNBDijetOutput[0], "Data", "PE")
        l5.AddEntry(hNBDijetOutput[8], "Fake-Fake", "F")
        l5.AddEntry(hNBDijetOutput[7], "Prompt-Fake", "F")
        l5.AddEntry(hNBDijetOutput[6], "Prompt-Prompt", "F")
        l5.Draw("SAME")
        c5.cd(2)
        c5.GetPad(2).SetPad(0.005, 0.005, 0.995, .25)
        temp4 = hNBDijetOutput[0].Clone()
        temp3 = hNBDijetOutput[8].Clone()
        temp4.Sumw2()
        temp3.Add(hNBDijetOutput[7])
        temp3.Add(hNBDijetOutput[6])
        temp4.Divide(temp3)
        temp4.Draw("PE")
        temp4.GetYaxis().SetRangeUser(0., 2.0)
        temp4.SetLineColor(ROOT.kBlue)
        temp4.SetMarkerColor(ROOT.kBlue)
        temp4.SetMarkerStyle(20)
        c5.GetPad(2).SetGridx(1)
        c5.GetPad(2).SetGridy(1)
        c5.SaveAs("dijetbdt_bg.png")
        c5.SaveAs("dijetbdt_bg.pdf")
    
        c6 = ROOT.TCanvas("c6", "c6", 800, 800)
        c6.Divide(1, 2)
        c6.cd(1)
        c6.GetPad(1).SetPad(0.005, 0.25, 0.995, .995)
        hNBCombinedOutput = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        #if (options.TeV == 8):
        bins = array.array('f', [float(i)/100.-1. for i in xrange(0, 21, 4)] + [-0.75, -0.7, -0.65, -0.60,-0.55, -0.5, -0.4,-0.3, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
        for z in [6,7,8,0]:
            hNBCombinedOutput[z] = variableBinning(ROOT.TH1F("hNBCombinedOutput"+str(z), "hNBCombinedOutput"+str(z), len(bins)-1, bins), hCombinedOutput[z], bins)
        #else:
        #    for z in [6,7,8,0]:
        #        hNBCombinedOutput[z] = hCombinedOutput[z]
        #        hCombinedOutput[z].Rebin(2)

        stackCombinedBg = ROOT.THStack("s3", "s3")
        hNBCombinedOutput[6].SetFillColor(ROOT.kGreen)
        hNBCombinedOutput[7].SetFillColor(ROOT.kYellow)
        hNBCombinedOutput[8].SetFillColor(ROOT.kRed)
        hCombinedOutput[0].Rebin(10)
        hCombinedOutput[6].Rebin(10)
        hCombinedOutput[7].Rebin(10)
        hCombinedOutput[8].Rebin(10)
        stackCombinedBg.Add(hNBCombinedOutput[6])
        stackCombinedBg.Add(hNBCombinedOutput[7])
        stackCombinedBg.Add(hNBCombinedOutput[8])
        stackCombinedBg.Draw("HIST")
        if (options.TeV == 7):
            stackCombinedBg.SetMaximum(900)
        else:
            stackCombinedBg.SetMaximum(5000)
        hNBCombinedOutput[0].SetMarkerStyle(20)
        hNBCombinedOutput[0].Draw("PESAME")
        stackCombinedBg.GetXaxis().SetTitle("BDT Classifier")
        stackCombinedBg.GetYaxis().SetTitle("# of events")
        stackCombinedBg.GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (not options.transform):
            lines = []
            for i in combinedCategories[0:-1]:
                lines.append(ROOT.TLine(i, 0, i, stackCombinedBg.GetMaximum()*0.8))
                lines[-1].Draw("SAME")

        l6 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l6 = ROOT.TLegend(0.45, 0.55, 0.88, 0.80)
        else:
            txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l6 = ROOT.TLegend(0.45, 0.55, 0.88, 0.80)
        l6.SetFillColor(ROOT.kWhite)
        l6.SetBorderSize(0)
        l6.AddEntry(hBDTOutput[0], "Data", "PE")
        l6.AddEntry(hBDTOutput[8], "Fake-Fake", "F")
        l6.AddEntry(hBDTOutput[7], "Prompt-Fake", "F")
        l6.AddEntry(hBDTOutput[6], "Prompt-Prompt", "F")
        l6.Draw("SAME")
        c6.cd(2)
        c6.GetPad(2).SetPad(0.005, 0.005, 0.995, .25)
        temp6 = hNBCombinedOutput[0].Clone()
        temp5 = hNBCombinedOutput[8].Clone()
        temp6.Sumw2()
        temp5.Add(hNBCombinedOutput[7])
        temp5.Add(hNBCombinedOutput[6])
        temp6.Divide(temp5)
        temp6.Draw("PE")
        temp6.GetYaxis().SetRangeUser(0., 2.0)
        temp6.SetLineColor(ROOT.kBlue)
        temp6.SetMarkerColor(ROOT.kBlue)
        temp6.SetMarkerStyle(20)
        c6.GetPad(2).SetGridx(1)
        c6.GetPad(2).SetGridy(1)
        c6.SaveAs("combinedbdt_bg.png")
        c6.SaveAs("combinedbdt_bg.pdf")

if __name__ == "__main__":
    if (options.TeV == 8):
        groupType = [[0], [3], [12,22,32,42], [11,21], [5], [-125000, -125100, -125400, -125500], [-38]]
        kfactors = [[0], [0.15], [0.20,0.20,0.20,0.20], [0.5,0.5], [0.04], [0., 0., 0., 0.]]
        # Jim Categories
        #bdtCategories = [-0.39, 0.13, 0.52, 0.75, 0.915, 1000]
        bdtCategories = [-0.78, -0.42, 0.0, 0.36, 0.76, 1000]
        combinedCategories = [0.14, 0.82, 0.94, 1000.]
        colors = [0, ROOT.kBlue-8, ROOT.kGreen-9, ROOT.kCyan, ROOT.kMagenta-10, ROOT.kRed]
        if (options.transform):
            f = ROOT.TFile("transformation.root")
            transformations.append(f.Get("Graph").Clone("diphomvaG"))
            transformations.append(f.Get("dijet").Clone("dijet"))
            f.Close()              
    else:
        groupType = [[0], [4, 14, 24], [12,22,32], [11,21], [5], [-125000, -125100, -125400, -125500], [-38]]
        kfactors = [[0], [0.15, 0.15, 0.15], [0.20,0.20,0.20], [0.5,0.5], [0.04], [0., 0., 0., 0.]]
        # Jim Categories
        #bdtCategories = [0.42, 0.79, 0.93, 0.975, 1000]
        bdtCategories = [0.19, 0.70, 0.85, 0.93, 1000]
        combinedCategories = [0.911, 0.992, 1000.]
        colors = [0, ROOT.kBlue-8, ROOT.kGreen-9, ROOT.kCyan, ROOT.kMagenta-10, ROOT.kRed]
        if (options.transform):
            f = ROOT.TFile("transformation.root")
            transformations.append(f.Get("dipho7TeV").Clone("dipho7TeV"))
            transformations.append(f.Get("dijet7TeV").Clone("dijet7TeV"))
            f.Close()              

    if (options.eventLooper):
        eventLoop()
    if (options.drawPlot):
        drawPlots()
