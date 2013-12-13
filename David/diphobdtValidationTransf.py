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
parser.add_option("-I","--inFile2",     default="opttree_8TeV_v2.root", help="Input file to be read. \nDefault: %default")
parser.add_option("-o","--outFile",     default="output.root", help="Output file to be produced. \nDefault: %default")
parser.add_option("-7","--TeV",         default=8, help="Number of photon categories for globe smearing. \nDefault: %default", type=int)
(options,arg) = parser.parse_args()

ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptStat(0)
#ROOT.gROOT.SetBatch(0)

transformations = []
hBDTOutput = []
hDijetOutput = []
hCombinedOutput = []
hTBDTOutput = []
hTDijetOutput = []
hTCombinedOutput = []
groupType = []
bdtCategories = []
colors = []
kfactors = []
binningsBDT = [] 
binningsDijet = [] 
binningsCombined = [] 

def transformX(hTot):
    q = array.array('d', [])
    probSum = array.array('d', [])
    for i in xrange(100):
        q.append(0.)
        probSum.append(float(i)/100.)
    hTot.GetQuantiles(100, q, probSum)
    q.append(1000.)
    return q

def readHistos():
    f = ROOT.TFile(options.inFile2)
    for i in xrange(9):
        hBDTOutput.append(f.Get("hBDTOutput"+str(i)))
        hDijetOutput.append(f.Get("hDijetOutput"+str(i)))
        hCombinedOutput.append(f.Get("hCombinedOutput"+str(i)))
 
    hTot1 = hBDTOutput[2].Clone()
    hTot1.Add(hBDTOutput[4])
    hTot1.Add(hBDTOutput[5])
    hTot1.Add(hBDTOutput[3])
    global binningsBDT 
    binningsBDT = transformX(hTot1)
    global binningsDijet
    binningsDijet = transformX(hDijetOutput[3])
    #for i in xrange(9):
    #    binningsBDT.append(transformX(hTot1, hBDTOutput[i]))
    #    print i
    #    print binningsBDT[-1]
    #    binningsBDT[-1].append(1000.)
        
def findBin(value, binning):
    bin = checkBDTCat(value, binning)
    #if (bin == 30):
    #    print bin, float(bin)/100.
    #    sys.exit()
    #print bin, float(bin)/100.
    #return 1-float(checkBDTCat(value, binning)+2)/100.
    return float(bin)/100.

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
    for i in xrange(9):
        hTBDTOutput.append(ROOT.TH1F("hTBDTOutput"+str(i), "hTBDTOutput"+str(i), 50, 0, 1))
        hTDijetOutput.append(ROOT.TH1F("hTDijetOutput"+str(i), "hTDijetOutput"+str(i), 50, 0, 1))
        hTCombinedOutput.append(ROOT.TH1F("hTCombinedOutput"+str(i), "hTCombinedOutput"+str(i), 50, 0, 1))

    infile = ROOT.TFile(options.inFile)
    tree = infile.Get("opttree")
    tree.SetBranchStatus("*", 0)
    tree.SetBranchStatus("ptoM1", 1)
    tree.SetBranchStatus("ptoM2", 1)
    tree.SetBranchStatus("idmva1", 1)
    tree.SetBranchStatus("idmva2", 1)
    tree.SetBranchStatus("mass", 1)
    tree.SetBranchStatus("itype", 1)
    tree.SetBranchStatus("full_weight", 1)
    tree.SetBranchStatus("dipho_mva", 1)
    tree.SetBranchStatus("dijet_Mjj", 1)
    tree.SetBranchStatus("dijet_LeadJPt", 1)
    tree.SetBranchStatus("dijet_SubJPt", 1)
    if (options.TeV == 7):
        tree.SetBranchStatus("bdt_dijet_7TeV_ptrewght", 1)
        tree.SetBranchStatus("bdt_combined_dijet7TeV_ptrewght", 1)
    else:
        tree.SetBranchStatus("bdt_dijet", 1)
        tree.SetBranchStatus("bdt_combined_dijet", 1)
         
    readHistos()

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
        dipho = transformations[0].Eval(tree.dipho_mva)
        dijet = -1#tree.bdt_dijet
        comb = -1#tree.bdt_combined_dijet
        if (options.TeV == 7):
            dijet = transformations[1].Eval(tree.bdt_dijet_7TeV_ptrewght)
            comb = tree.bdt_combined_dijet7TeV_ptrewght
        else:
            dijet = transformations[1].Eval(tree.bdt_dijet)
            comb = tree.bdt_combined_dijet
               
        newvalue = 1 - (findBin(dipho, binningsBDT) + 0.0005)
        newDijet = 1 - (findBin(dijet, binningsDijet) + 0.0005)
        #print newDijet, binningsDijet
        if (tree.itype == 0):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                hTDijetOutput[0].Fill(newDijet, weight)
                hTCombinedOutput[0].Fill(comb, weight)
            hTBDTOutput[0].Fill(newvalue, weight)    
        elif (tree.itype > 0):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                hTDijetOutput[1].Fill(newDijet, weight)
                hTCombinedOutput[1].Fill(comb, weight)
            hTBDTOutput[1].Fill(newvalue, weight)
        
            sampleCat, typeInd = checkSampleCat(groupType, tree.itype)
            if (sampleCat > 0 and sampleCat < 4):
                if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                    hTDijetOutput[5+sampleCat].Fill(newDijet, weight)
                    hTCombinedOutput[5+sampleCat].Fill(comb, weight)
                hTBDTOutput[5+sampleCat].Fill(newvalue, weight)
        elif (tree.itype == -125000):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                hTDijetOutput[2].Fill(newDijet, weight)
                hTCombinedOutput[2].Fill(comb, weight)    
            hTBDTOutput[2].Fill(newvalue, weight)
        elif (tree.itype == -125100):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                hTDijetOutput[3].Fill(newDijet, weight)
                hTCombinedOutput[3].Fill(comb, weight)
            hTBDTOutput[3].Fill(newvalue, weight)
        elif (tree.itype == -125400):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                hTDijetOutput[4].Fill(newDijet, weight)
                hTCombinedOutput[4].Fill(comb, weight)
            hTBDTOutput[4].Fill(newvalue, weight)
        elif (tree.itype == -125500):
            if (tree.dijet_Mjj > 250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20.):
                hTDijetOutput[5].Fill(newDijet, weight)
                hTCombinedOutput[5].Fill(comb, weight)
            hTBDTOutput[5].Fill(newvalue, weight)
    all_histos = hTBDTOutput + hTDijetOutput + hTCombinedOutput
    output = ROOT.TFile(options.outFile, "recreate")
    for h in all_histos:
        h.Write()
    output.Close()

            
def drawPlots():
    if (options.drawPlot):
        readHistos()
        f1 = ROOT.TFile(options.inFile)
        for i in xrange(9):
            hTBDTOutput.append(f1.Get("hTBDTOutput"+str(i)))
            hTDijetOutput.append(f1.Get("hTDijetOutput"+str(i)))

    c2 = ROOT.TCanvas("c2", "c2")
    colors = [ROOT.kRed, ROOT.kYellow, ROOT.kGreen, ROOT.kBlue]
    for j,z in enumerate((2,3,4, 5)):
        hTBDTOutput[z].SetLineColor(colors[j])
        hTBDTOutput[z].SetMarkerStyle(20)
        hTBDTOutput[z].SetMarkerColor(colors[j])
        hTBDTOutput[z].SetMarkerSize(0.75)
        hTBDTOutput[z].Scale(1./hTBDTOutput[z].Integral())
        if (j == 0):
            hTBDTOutput[z].GetYaxis().SetRangeUser(0, 0.25)
            hTBDTOutput[z].Draw("P")
            hTBDTOutput[z].GetXaxis().SetTitle("(1-#epsilon_{sig}) Transformed BDT Classifier")
            hTBDTOutput[z].GetYaxis().SetTitle("# of events/0.02")
            hTBDTOutput[z].GetYaxis().SetTitleOffset(1.2)
        else:
            hTBDTOutput[z].Draw("PSAME")
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        l2 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.60, 0.60, 0.78)
        else:
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.60, 0.60, 0.78)
        l2.SetFillColor(ROOT.kWhite)
        l2.SetBorderSize(0)
        l2.AddEntry(hTBDTOutput[2], "GF (m_{H}=125 GeV)", "PE")
        l2.AddEntry(hTBDTOutput[3], "VBF", "PE")
        l2.AddEntry(hTBDTOutput[4], "WH/ZH", "PE")
        l2.AddEntry(hTBDTOutput[5], "ttH", "PE")
        l2.Draw("SAME")
    c2.SaveAs("diphobdt_signal_transformed.png")

    c3 = ROOT.TCanvas("c2", "c2")
    colors = [ROOT.kGreen, ROOT.kYellow, ROOT.kRed, ROOT.kBlack]
    c3.SetLogy()
    tempSum = ""
    stackDiphoBDT = ROOT.THStack("s1", "s1")
    for j,z in enumerate((6,7,8,0)):
        hTBDTOutput[z].SetFillColor(colors[j])
        hTBDTOutput[z].SetMarkerStyle(20)
        hTBDTOutput[z].SetMarkerColor(colors[j])
        hTBDTOutput[z].SetMarkerSize(0.75)
        if (z != 0):
            stackDiphoBDT.Add(hTBDTOutput[z])
            if (j==0):
                tempSum = hTBDTOutput[z].Clone()
            else:
                tempSum.Add(hTBDTOutput[z])
    hTBDTOutput[6].Scale(1./tempSum.Integral())
    hTBDTOutput[7].Scale(1./tempSum.Integral())
    hTBDTOutput[8].Scale(1./tempSum.Integral())
    hTBDTOutput[0].Sumw2()
    hTBDTOutput[0].Scale(1./hTBDTOutput[0].Integral())
    stackDiphoBDT.Draw()
    stackDiphoBDT.SetMaximum(1.0)
    stackDiphoBDT.GetXaxis().SetTitle("(1-#epsilon_{sig}) Transformed BDT Classifier")
    stackDiphoBDT.GetYaxis().SetTitle("# of events/0.02")
    stackDiphoBDT.GetYaxis().SetTitleOffset(1.2)
    hTBDTOutput[0].Draw("PESAME")
    txt1 = ROOT.TLatex()
    txt1.SetNDC()
    txt1.SetTextSize(0.05)
    txt1.SetTextAlign(12)
    l2 = ""
    if (options.TeV == 8):
        txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
        l2 = ROOT.TLegend(0.45, 0.60, 0.85, 0.78)
    else:
        txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
        l2 = ROOT.TLegend(0.15, 0.60, 0.60, 0.78)
    l2.SetFillColor(ROOT.kWhite)
    l2.SetBorderSize(0)
    l2.AddEntry(hTBDTOutput[0], "Data", "PE")
    l2.AddEntry(hTBDTOutput[6], "Prompt-Prompt", "F")
    l2.AddEntry(hTBDTOutput[7], "Prompt-Fake", "F")
    l2.AddEntry(hTBDTOutput[8], "Fake-Fake", "F")
    l2.Draw("SAME")
    c3.SaveAs("diphobdt_bg_transformed.png")

    c4 = ROOT.TCanvas("c4", "c4")
    colors = [ROOT.kRed, ROOT.kYellow, ROOT.kGreen, ROOT.kBlue]
    for j,z in enumerate((2,3,4,5)):
        hTDijetOutput[z].SetLineColor(colors[j])
        hTDijetOutput[z].SetMarkerStyle(20)
        hTDijetOutput[z].SetMarkerColor(colors[j])
        hTDijetOutput[z].SetMarkerSize(0.75)
        #if (hTDijetOutput[z].Integral() != 0):
        hTDijetOutput[z].Scale(1./hTDijetOutput[z].Integral())
        if (j == 0):
            hTDijetOutput[z].GetYaxis().SetRangeUser(0, 0.25)
            hTDijetOutput[z].Draw("P")
            hTDijetOutput[z].GetXaxis().SetTitle("(1-#epsilon_{sig}) Transformed BDT Classifier")
            hTDijetOutput[z].GetYaxis().SetTitle("# of events/0.02")
            hTDijetOutput[z].GetYaxis().SetTitleOffset(1.2)
        else:
            hTDijetOutput[z].Draw("PSAME")
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        l2 = ""
        if (options.TeV == 8):
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.60, 0.60, 0.78)
        else:
            txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            l2 = ROOT.TLegend(0.15, 0.60, 0.60, 0.78)
        l2.SetFillColor(ROOT.kWhite)
        l2.SetBorderSize(0)
        l2.AddEntry(hTDijetOutput[2], "GF (m_{H}=125 GeV)", "PE")
        l2.AddEntry(hTDijetOutput[3], "VBF", "PE")
        l2.AddEntry(hTDijetOutput[4], "WH/ZH", "PE")
        l2.AddEntry(hTDijetOutput[5], "ttH", "PE")
        l2.Draw("SAME")
    c4.SaveAs("dijetbdt_signal_transformed.png")

    c5 = ROOT.TCanvas("c5", "c5")
    colors = [ROOT.kGreen, ROOT.kYellow, ROOT.kRed, ROOT.kBlack]
    c5.SetLogy()
    tempSum = ""
    stackDijetBDT = ROOT.THStack("s2", "s2")
    for j,z in enumerate((6,7,8,0)):
        hTDijetOutput[z].SetFillColor(colors[j])
        hTDijetOutput[z].SetMarkerStyle(20)
        hTDijetOutput[z].SetMarkerColor(colors[j])
        hTDijetOutput[z].SetMarkerSize(0.75)
        if (z != 0):
            stackDijetBDT.Add(hTDijetOutput[z])
            if (j==0):
                tempSum = hTDijetOutput[z].Clone()
            else:
                tempSum.Add(hTDijetOutput[z])
    hTDijetOutput[6].Scale(1./tempSum.Integral())
    hTDijetOutput[7].Scale(1./tempSum.Integral())
    hTDijetOutput[8].Scale(1./tempSum.Integral())
    hTDijetOutput[0].Sumw2()
    hTDijetOutput[0].Scale(1./hTDijetOutput[0].Integral())
    stackDijetBDT.Draw()
    stackDijetBDT.SetMaximum(1.0)
    stackDijetBDT.GetXaxis().SetTitle("(1-#epsilon_{sig}) Transformed BDT Classifier")
    stackDijetBDT.GetYaxis().SetTitle("# of events/0.02")
    stackDijetBDT.GetYaxis().SetTitleOffset(1.2)
    hTDijetOutput[0].Draw("PESAME")
    txt1 = ROOT.TLatex()
    txt1.SetNDC()
    txt1.SetTextSize(0.05)
    txt1.SetTextAlign(12)
    l2 = ""
    if (options.TeV == 8):
        txt1.DrawLatex(0.45, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
        l2 = ROOT.TLegend(0.45, 0.60, 0.85, 0.78)
    else:
        txt1.DrawLatex(0.15, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
        l2 = ROOT.TLegend(0.15, 0.60, 0.60, 0.78)
    l2.SetFillColor(ROOT.kWhite)
    l2.SetBorderSize(0)
    l2.AddEntry(hTDijetOutput[0], "Data", "PE")
    l2.AddEntry(hTDijetOutput[6], "Prompt-Prompt", "F")
    l2.AddEntry(hTDijetOutput[7], "Prompt-Fake", "F")
    l2.AddEntry(hTDijetOutput[8], "Fake-Fake", "F")
    l2.Draw("SAME")
    c5.SaveAs("dijetbdt_bg_transformed.png")

if __name__ == "__main__":
    if (options.TeV == 8):
        groupType = [[0], [3], [12,22,32,42], [11,21], [5], [-125000, -125100, -125400, -125500]]
        kfactors = [[0], [0.15], [0.20,0.20,0.20,0.20], [0.5,0.5], [0.04], [0., 0., 0., 0.]]
        # Jim Categories
        #bdtCategories = [-0.39, 0.13, 0.52, 0.75, 0.915, 1000]
        bdtCategories = [-0.78, -0.42, 0.0, 0.36, 0.76, 1000]
        colors = [0, ROOT.kBlue-8, ROOT.kGreen-9, ROOT.kCyan, ROOT.kMagenta-10, ROOT.kRed]
        f = ROOT.TFile("transformation.root")
        transformations.append(f.Get("Graph").Clone("diphomvaG"))
        transformations.append(f.Get("dijet").Clone("dijet"))
        f.Close()              
    else:
        groupType = [[0], [4, 14, 24], [12,22,32], [11,21], [5], [-125000, -125100, -125400, -125500]]
        kfactors = [[0], [0.15, 0.15, 0.15], [0.20,0.20,0.20], [0.5,0.5], [0.04], [0., 0., 0., 0.]]
        # Jim Categories
        #bdtCategories = [0.42, 0.79, 0.93, 0.975, 1000]
        bdtCategories = [0.19, 0.70, 0.85, 0.93, 1000]
        colors = [0, ROOT.kBlue-8, ROOT.kGreen-9, ROOT.kCyan, ROOT.kMagenta-10, ROOT.kRed]
        f = ROOT.TFile("transformation.root")
        transformations.append(f.Get("dipho7TeV").Clone("dipho7TeV"))
        transformations.append(f.Get("dijet7TeV").Clone("dijet7TeV"))
        f.Close()              

    if (not options.drawPlot):
        eventLoop()
        drawPlots()
    else:
        drawPlots()
