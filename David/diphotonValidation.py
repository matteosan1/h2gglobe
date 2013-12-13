import ROOT
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d","--drawPlot",    default=False, help="Draw plots. \nDefault: %default", action="store_true")
parser.add_option("-b","--blinding",    default=False, help="Draw blinded plots. \nDefault: %default", action="store_true")
parser.add_option("-l","--eventLooper", default=False, help="Loop on the events. \nDefault: %default", action="store_true")
parser.add_option("-i","--inFile",      default="opttree_8TeV_v2.root", help="Input file to be read. \nDefault: %default")
parser.add_option("-o","--outFile",     default="output.root", help="Output file to be produced. \nDefault: %default")
parser.add_option("-7","--TeV",         default=8, help="Number of photon categories for globe smearing. \nDefault: %default", type=int)
(options,arg) = parser.parse_args()

ROOT.gStyle.SetOptTitle(0)
#ROOT.gROOT.SetBatch(0)

hCiCIncError  = []
hCiCIncMass   = []
hBDTIncError  = []
hBDTIncMass   = []
hCiCError     = []
hCiCMass      = []
hCiCLowError  = []
hCiCLowMass   = []
hCiCHighError = []
hCiCHighMass  = []
hBDTError     = []
hBDTMass      = []

groupType     = []
bdtCategories = []
colors        = []
kfactors      = []

def r9Scaling(r9, eta):
    r9new = -1
    if (options.TeV == 7):
        if (abs(eta)<1.479):
            r9new = 0.000854+r9*1.00153
        else:
            r9new = 0.001231+r9*1.00050
    else:
        if (abs(eta)<1.479):
            r9new = 0.000740+r9*1.00139
        else:
            r9new = -0.000399+r9*1.00016

    return r9new

def readHistos(f):
    for i in xrange(len(groupType)):
        hCiCIncError.append(f.Get("hCiCIncError"+str(i)))
        hCiCIncMass.append(f.Get("hCiCIncMass"+str(i)))
        hBDTIncError.append(f.Get("hBDTIncError"+str(i)))
        hBDTIncMass.append(f.Get("hBDTIncMass"+str(i)))
    for i in xrange(4):
        for j in xrange(len(groupType)):
            hCiCMass.append(f.Get("hCiCMass"+str(i)+"_cat"+str(j)))
            hCiCError.append(f.Get("hCiCError"+str(i)+"_cat"+str(j)))
    for i in xrange(4):
        for j in xrange(len(groupType)):
            hCiCLowMass.append(f.Get("hCiCLowMass"+str(i)+"_cat"+str(j)))
            hCiCLowError.append(f.Get("hCiCLowError"+str(i)+"_cat"+str(j)))
    for i in xrange(4):
        for j in xrange(len(groupType)):
            hCiCHighMass.append(f.Get("hCiCHighMass"+str(i)+"_cat"+str(j)))
            hCiCHighError.append(f.Get("hCiCHighError"+str(i)+"_cat"+str(j)))

    for i in xrange(len(bdtCategories)-1):
        for j in xrange(len(groupType)):
            hBDTMass.append(f.Get("hBDTMass"+str(i)+"_cat"+str(j)))
            hBDTError.append(f.Get("hBDTError"+str(i)+"_cat"+str(j)))

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
    for i in xrange(len(groupType)):
        hCiCIncError.append(ROOT.TH1F("hCiCIncError"+str(i), "hCiCIncError"+str(i), 40, 100, 180))
        hCiCIncMass.append(ROOT.TH1F("hCiCIncMass"+str(i), "hCiCIncMass"+str(i), 40, 100, 180))
        hCiCIncMass[-1].SetMarkerStyle(20)
        if (i != len(groupType)-1):
            hCiCIncMass[-1].SetFillColor(colors[i])
        else:
            hCiCIncMass[-1].SetLineColor(colors[i])
            hCiCIncMass[-1].SetLineWidth(2)
        hBDTIncError.append(ROOT.TH1F("hBDTIncError"+str(i), "hBDTIncError"+str(i), 40, 100, 180))
        hBDTIncMass.append(ROOT.TH1F("hBDTIncMass"+str(i), "hBDTIncMass"+str(i), 40, 100, 180))
        hBDTIncMass[-1].SetMarkerStyle(20)
        if (i != len(groupType)-1):
            hBDTIncMass[-1].SetFillColor(colors[i])
        else:
            hBDTIncMass[-1].SetLineColor(colors[i])
            hBDTIncMass[-1].SetLineWidth(2)

    for i in xrange(4):
        for j in xrange(len(groupType)):
            hCiCMass.append(ROOT.TH1F("hCiCMass"+str(i)+"_cat"+str(j), "hCiCMass"+str(i)+"_cat"+str(j), 40, 100, 180))
            hCiCError.append(ROOT.TH1F("hCiCError"+str(i)+"_cat"+str(j), "hCiCError"+str(i)+"_cat"+str(j), 40, 100, 180))
            hCiCMass[-1].SetMarkerStyle(20)
            if (j != len(groupType)-1):
                hCiCMass[-1].SetFillColor(colors[j])
            else:
                hCiCMass[-1].SetLineColor(colors[j])
                hCiCMass[-1].SetLineWidth(2)

    for i in xrange(4):
        for j in xrange(len(groupType)):
            hCiCLowMass.append(ROOT.TH1F("hCiCLowMass"+str(i)+"_cat"+str(j), "hCiCLowMass"+str(i)+"_cat"+str(j), 40, 100, 180))
            hCiCLowError.append(ROOT.TH1F("hCiCLowError"+str(i)+"_cat"+str(j), "hCiCLowError"+str(i)+"_cat"+str(j), 40, 100, 180))
            hCiCLowMass[-1].SetMarkerStyle(20)
            if (j != len(groupType)-1):
                hCiCLowMass[-1].SetFillColor(colors[j])
            else:
                hCiCLowMass[-1].SetLineColor(colors[j])
                hCiCLowMass[-1].SetLineWidth(2)

    for i in xrange(4):
        for j in xrange(len(groupType)):
            hCiCHighMass.append(ROOT.TH1F("hCiCHighMass"+str(i)+"_cat"+str(j), "hCiCHighMass"+str(i)+"_cat"+str(j), 40, 100, 180))
            hCiCHighError.append(ROOT.TH1F("hCiCHighError"+str(i)+"_cat"+str(j), "hCiCHighError"+str(i)+"_cat"+str(j), 40, 100, 180))
            hCiCHighMass[-1].SetMarkerStyle(20)
            if (j != len(groupType)-1):
                hCiCHighMass[-1].SetFillColor(colors[j])
            else:
                hCiCHighMass[-1].SetLineColor(colors[j])
                hCiCHighMass[-1].SetLineWidth(2)

    for i in xrange(len(bdtCategories)-1):
        for j in xrange(len(groupType)):
            hBDTMass.append(ROOT.TH1F("hBDTMass"+str(i)+"_cat"+str(j), "hBDTMass"+str(i)+"_cat"+str(j), 40, 100, 180))
            hBDTError.append(ROOT.TH1F("hBDTError"+str(i)+"_cat"+str(j), "hBDTError"+str(i)+"_cat"+str(j), 40, 100, 180))
            hBDTMass[-1].SetMarkerStyle(20)
            if (j != len(groupType)-1):
                hBDTMass[-1].SetFillColor(colors[j])
            else:
                hBDTMass[-1].SetLineColor(colors[j])
                hBDTMass[-1].SetLineWidth(2)
            
    infile = ROOT.TFile(options.inFile)
    tree = infile.Get("opttree")

    entries = tree.GetEntries()
    print "File entries: ", entries
    for z in xrange(entries):
        tree.GetEntry(z)

        if (z%100000 == 0):
            print z
    
        sampleCat, typeInd = checkSampleCat(groupType, tree.itype)
        if (sampleCat == -1):
            continue

        if (tree.ptoM1 < 0.33 or tree.ptoM2 < 0.25):
            continue
        
        weight = tree.full_weight
        # hack for Sherpa 8 TeV
        if (tree.itype == 3):
            weight = weight*0.85

        if (tree.itype == 0 and tree.mass<150 and tree.mass >110 and options.blinding):
            continue

        if (tree.cicpf4cutlevel1 > 3 and tree.cicpf4cutlevel2>3):
            hCiCIncError[sampleCat].Fill(tree.mass, weight*kfactors[sampleCat][typeInd])
            hCiCIncMass[sampleCat].Fill(tree.mass, weight)
            if (not(tree.dijet_Mjj>250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20)):
                cicCat = checkCiCCat(tree.eta1, r9Scaling(tree.r91, tree.eta1), tree.eta2, r9Scaling(tree.r92, tree.eta2))
                hCiCMass[sampleCat+cicCat*len(groupType)].Fill(tree.mass, weight)
                hCiCError[sampleCat+cicCat*len(groupType)].Fill(tree.mass, weight*kfactors[sampleCat][typeInd])
                if (tree.dipho_pt/tree.mass > (40./125.)):
                    cicCat = checkCiCCat(tree.eta1, r9Scaling(tree.r91, tree.eta1), tree.eta2, r9Scaling(tree.r92, tree.eta2))
                    hCiCHighMass[sampleCat+cicCat*len(groupType)].Fill(tree.mass, weight)
                    hCiCHighError[sampleCat+cicCat*len(groupType)].Fill(tree.mass, weight*kfactors[sampleCat][typeInd])
                if (tree.dipho_pt/tree.mass < (40./125.)):
                    cicCat = checkCiCCat(tree.eta1, r9Scaling(tree.r91, tree.eta1), tree.eta2, r9Scaling(tree.r92, tree.eta2))
                    hCiCLowMass[sampleCat+cicCat*len(groupType)].Fill(tree.mass, weight)
                    hCiCLowError[sampleCat+cicCat*len(groupType)].Fill(tree.mass, weight*kfactors[sampleCat][typeInd])

        if (tree.dipho_mva > bdtCategories[0] and tree.idmva1 > -0.2 and tree.idmva2 > -0.2):
            hBDTIncMass[sampleCat].Fill(tree.mass, weight)
            hBDTIncError[sampleCat].Fill(tree.mass, weight*kfactors[sampleCat][typeInd])
            if (not(tree.dijet_Mjj>250 and tree.dijet_LeadJPt>30 and tree.dijet_SubJPt>20)):
                bdtCat = checkBDTCat(tree.dipho_mva, bdtCategories)
                hBDTMass[sampleCat+bdtCat*len(groupType)].Fill(tree.mass, weight)
                hBDTError[sampleCat+bdtCat*len(groupType)].Fill(tree.mass, weight*kfactors[sampleCat][typeInd])
    
    all_histos = hCiCIncError + hCiCIncMass + hBDTIncError + hBDTIncMass + hCiCMass + hBDTMass + hCiCError + hBDTError + hCiCLowMass + hCiCLowError + hCiCHighMass + hCiCHighError
    output = ROOT.TFile(options.outFile, "recreate")
    for h in all_histos:
        h.Write()
    output.Close()

def drawPlots():
    inputFile = ROOT.TFile(options.inFile)
    readHistos(inputFile)

    c1 = ROOT.TCanvas("c1", "c1", 800, 600)
    temp = hCiCIncMass[1].Clone()
    stackCiCIncMass = ROOT.THStack("s1", "s1")
    for i in xrange(1, len(groupType)-1):    
        stackCiCIncMass.Add(hCiCIncMass[i])
        if (i != 1):
            hCiCIncError[1].Add(hCiCIncError[i])
            temp.Add(hCiCIncMass[i])
    stackCiCIncMass.Draw()
    maximum = stackCiCIncMass.GetMaximum()*1.3
    stackCiCIncMass.SetMaximum(maximum)
    hCiCIncMass[0].Draw("PESAME")
    hCiCIncMass[-1].Scale(5)
    hCiCIncMass[-1].Draw("SAME")
    for i in xrange(1, temp.GetXaxis().GetNbins()+1):
        temp.SetBinError(i, hCiCIncError[1].GetBinContent(i))
    temp.Draw("E2SAME")
    temp.SetFillColor(ROOT.kBlack)
    temp.SetFillStyle(3004)
    temp.SetMarkerStyle(0)
    stackCiCIncMass.GetXaxis().SetTitle("m_{#gamma#gamma} (GeV)")
    stackCiCIncMass.GetYaxis().SetTitle("Events/2 GeV")
    stackCiCIncMass.GetYaxis().SetTitleOffset(1.2)

    txt1 = ROOT.TLatex()
    txt1.SetNDC()
    txt1.SetTextSize(0.05)
    txt1.SetTextAlign(12)
    if (options.TeV == 8):
        txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
    else:
        txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
    
    l1 = ROOT.TLegend(0.60, 0.65, 0.88, 0.88)
    l1.SetFillColor(ROOT.kWhite)
    l1.SetBorderSize(0)
    l1.AddEntry(hCiCIncMass[0], "Data", "PE")
    l1.AddEntry(hCiCIncMass[1], "2 prompt #gamma", "F")
    l1.AddEntry(hCiCIncMass[2], "1 prompt #gamma 1 fake #gamma", "F")
    l1.AddEntry(hCiCIncMass[3], "2 fake #gamma", "F")
    l1.AddEntry(hCiCIncMass[4], "Drell-Yan", "F")
    l1.AddEntry(hCiCIncMass[5], "H#rightarrow#gamma#gamma(125 GeV) x5", "F")
    l1.Draw("SAME")
    c1.SaveAs("incMassCiC.pdf")
    c1.SaveAs("incMassCiC.png")

    c2 = ROOT.TCanvas("c2", "c2", 800, 600)
    stackBDTIncMass = ROOT.THStack("s2", "s2")
    temp1 = hBDTIncMass[1].Clone()
    for i in xrange(1, len(groupType)-1):    
        stackBDTIncMass.Add(hBDTIncMass[i])
        if (i != 1):
            hBDTIncError[1].Add(hBDTIncError[i])
            temp1.Add(hBDTIncMass[i])
    stackBDTIncMass.Draw()
    maximum = stackBDTIncMass.GetMaximum()*1.3
    stackBDTIncMass.SetMaximum(maximum)
    hBDTIncMass[0].Draw("PESAME")
    hBDTIncMass[-1].Scale(5)
    hBDTIncMass[-1].Draw("SAME")
    for i in xrange(1, temp1.GetXaxis().GetNbins()+1):
        temp1.SetBinError(i, hBDTIncError[1].GetBinContent(i))
    temp1.Draw("E2SAME")
    temp1.SetFillColor(ROOT.kBlack)
    temp1.SetFillStyle(3004)
    temp1.SetMarkerStyle(0)
    stackBDTIncMass.GetXaxis().SetTitle("m_{#gamma#gamma} (GeV)")
    stackBDTIncMass.GetYaxis().SetTitle("Events/2 GeV")
    stackBDTIncMass.GetYaxis().SetTitleOffset(1.2)
    txt2 = ROOT.TLatex()
    txt2.SetNDC()
    txt2.SetTextSize(0.05)
    txt2.SetTextAlign(12)
    if (options.TeV == 8):
        txt2.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
    else:
        txt2.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")

    l2 = ROOT.TLegend(0.60, 0.65, 0.88, 0.88)
    l2.SetFillColor(ROOT.kWhite)
    l2.SetBorderSize(0)
    l2.AddEntry(hCiCIncMass[0], "Data", "PE")
    l2.AddEntry(hCiCIncMass[1], "2 prompt #gamma", "F")
    l2.AddEntry(hCiCIncMass[2], "1 prompt #gamma 1 fake #gamma", "F")
    l2.AddEntry(hCiCIncMass[3], "2 fake #gamma", "F")
    l2.AddEntry(hCiCIncMass[4], "Drell-Yan", "F")
    l2.AddEntry(hCiCIncMass[5], "H#rightarrow#gamma#gamma(125 GeV) x5", "F")
    l2.Draw("SAME")
    c2.SaveAs("incMassBDT.pdf")
    c2.SaveAs("incMassBDT.png")

    c3 = ROOT.TCanvas("c3", "c3", 800, 800)
    c3.Divide(2,2)
    stackCiCMass = []
    temp2 = []
    l3 = []
    for c in xrange(4):
        c3.cd(c+1)
        stackCiCMass.append(ROOT.THStack("s3"+str(c), "s3"+str(c)))
        temp2.append(hCiCMass[1+c*len(groupType)].Clone())
        for i in xrange(1, len(groupType)-1):    
            stackCiCMass[-1].Add(hCiCMass[i+c*len(groupType)])
            if (i != 1):
                hCiCError[1].Add(hCiCError[i+c*len(groupType)])
                temp2[-1].Add(hCiCMass[i+c*len(groupType)])
        stackCiCMass[-1].Draw()
        maximum = stackCiCMass[-1].GetMaximum()*1.3
        stackCiCMass[-1].SetMaximum(maximum)
        hCiCMass[c*len(groupType)].Draw("PESAME")
        hCiCMass[len(groupType)-1+c*len(groupType)].Scale(5)
        hCiCMass[len(groupType)-1+c*len(groupType)].Draw("SAME")
        for i in xrange(1, temp2[-1].GetXaxis().GetNbins()+1):
            temp2[-1].SetBinError(i, hCiCError[1+c*len(groupType)].GetBinContent(i))
        temp2[-1].Draw("E2SAME")
        temp2[-1].SetFillColor(ROOT.kBlack)
        temp2[-1].SetFillStyle(3004)
        temp2[-1].SetMarkerStyle(0)
        stackCiCMass[-1].GetXaxis().SetTitle("m_{#gamma#gamma} (GeV)")
        stackCiCMass[-1].GetYaxis().SetTitle("Events/2 GeV")
        stackCiCMass[-1].GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (options.TeV == 8):
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
        else:
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            
        l3.append(ROOT.TLegend(0.60, 0.65, 0.88, 0.88))
        l3[-1].SetFillColor(ROOT.kWhite)
        l3[-1].SetBorderSize(0)
        l3[-1].AddEntry(hCiCMass[0], "Data", "PE")
        l3[-1].AddEntry(hCiCMass[1], "2 prompt #gamma", "F")
        l3[-1].AddEntry(hCiCMass[2], "1 prompt #gamma 1 fake #gamma", "F")
        l3[-1].AddEntry(hCiCMass[3], "2 fake #gamma", "F")
        l3[-1].AddEntry(hCiCMass[4], "Drell-Yan", "F")
        l3[-1].AddEntry(hCiCMass[5], "H#rightarrow#gamma#gamma(125 GeV) x5", "F")
        l3[-1].Draw("SAME")
    c3.SaveAs("massCiCCats.pdf")
    c3.SaveAs("massCiCCats.png")
    
    c31 = ROOT.TCanvas("c31", "c31", 800, 800)
    c31.Divide(2,2)
    stackCiCHighMass = []
    temp21 = []
    l31 = []
    for c in xrange(4):
        c31.cd(c+1)
        stackCiCHighMass.append(ROOT.THStack("s31"+str(c), "s31"+str(c)))
        temp21.append(hCiCHighMass[1+c*len(groupType)].Clone())
        for i in xrange(1, len(groupType)-1):    
            stackCiCHighMass[-1].Add(hCiCHighMass[i+c*len(groupType)])
            if (i != 1):
                hCiCHighError[1].Add(hCiCHighError[i+c*len(groupType)])
                temp21[-1].Add(hCiCHighMass[i+c*len(groupType)])
        stackCiCHighMass[-1].Draw()
        maximum = stackCiCHighMass[-1].GetMaximum()*1.3
        stackCiCHighMass[-1].SetMaximum(maximum)
        hCiCHighMass[c*len(groupType)].Draw("PESAME")
        hCiCHighMass[len(groupType)-1+c*len(groupType)].Scale(5)
        hCiCHighMass[len(groupType)-1+c*len(groupType)].Draw("SAME")
        for i in xrange(1, temp21[-1].GetXaxis().GetNbins()+1):
            temp21[-1].SetBinError(i, hCiCHighError[1+c*len(groupType)].GetBinContent(i))
        temp21[-1].Draw("E2SAME")
        temp21[-1].SetFillColor(ROOT.kBlack)
        temp21[-1].SetFillStyle(3004)
        temp21[-1].SetMarkerStyle(0)
        stackCiCHighMass[-1].GetXaxis().SetTitle("m_{#gamma#gamma} (GeV)")
        stackCiCHighMass[-1].GetYaxis().SetTitle("Events/2 GeV")
        stackCiCHighMass[-1].GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (options.TeV == 8):
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
        else:
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            
        l31.append(ROOT.TLegend(0.60, 0.65, 0.88, 0.88))
        l31[-1].SetFillColor(ROOT.kWhite)
        l31[-1].SetBorderSize(0)
        l31[-1].AddEntry(hCiCHighMass[0], "Data", "PE")
        l31[-1].AddEntry(hCiCHighMass[1], "2 prompt #gamma", "F")
        l31[-1].AddEntry(hCiCHighMass[2], "1 prompt #gamma 1 fake #gamma", "F")
        l31[-1].AddEntry(hCiCHighMass[3], "2 fake #gamma", "F")
        l31[-1].AddEntry(hCiCHighMass[4], "Drell-Yan", "F")
        l31[-1].AddEntry(hCiCHighMass[5], "H#rightarrow#gamma#gamma(125 GeV) x5", "F")
        l31[-1].Draw("SAME")
    c31.SaveAs("massCiCHighCats.pdf")
    c31.SaveAs("massCiCHighCats.png")

    c32 = ROOT.TCanvas("c32", "c32", 800, 800)
    c32.Divide(2,2)
    stackCiCLowMass = []
    temp22 = []
    l32 = []
    for c in xrange(4):
        c32.cd(c+1)
        stackCiCLowMass.append(ROOT.THStack("s32"+str(c), "s32"+str(c)))
        temp22.append(hCiCLowMass[1+c*len(groupType)].Clone())
        for i in xrange(1, len(groupType)-1):    
            stackCiCLowMass[-1].Add(hCiCLowMass[i+c*len(groupType)])
            if (i != 1):
                hCiCLowError[1].Add(hCiCLowError[i+c*len(groupType)])
                temp22[-1].Add(hCiCLowMass[i+c*len(groupType)])
        stackCiCLowMass[-1].Draw()
        maximum = stackCiCLowMass[-1].GetMaximum()*1.3
        stackCiCLowMass[-1].SetMaximum(maximum)
        hCiCLowMass[c*len(groupType)].Draw("PESAME")
        hCiCLowMass[len(groupType)-1+c*len(groupType)].Scale(5)
        hCiCLowMass[len(groupType)-1+c*len(groupType)].Draw("SAME")
        for i in xrange(1, temp2[-1].GetXaxis().GetNbins()+1):
            temp22[-1].SetBinError(i, hCiCLowError[1+c*len(groupType)].GetBinContent(i))
        temp22[-1].Draw("E2SAME")
        temp22[-1].SetFillColor(ROOT.kBlack)
        temp22[-1].SetFillStyle(3004)
        temp22[-1].SetMarkerStyle(0)
        stackCiCLowMass[-1].GetXaxis().SetTitle("m_{#gamma#gamma} (GeV)")
        stackCiCLowMass[-1].GetYaxis().SetTitle("Events/2 GeV")
        stackCiCLowMass[-1].GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (options.TeV == 8):
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
        else:
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            
        l32.append(ROOT.TLegend(0.60, 0.65, 0.88, 0.88))
        l32[-1].SetFillColor(ROOT.kWhite)
        l32[-1].SetBorderSize(0)
        l32[-1].AddEntry(hCiCMass[0], "Data", "PE")
        l32[-1].AddEntry(hCiCMass[1], "2 prompt #gamma", "F")
        l32[-1].AddEntry(hCiCMass[2], "1 prompt #gamma 1 fake #gamma", "F")
        l32[-1].AddEntry(hCiCMass[3], "2 fake #gamma", "F")
        l32[-1].AddEntry(hCiCMass[4], "Drell-Yan", "F")
        l32[-1].AddEntry(hCiCMass[5], "H#rightarrow#gamma#gamma(125 GeV) x5", "F")
        l32[-1].Draw("SAME")
    c32.SaveAs("massCiCLowCats.pdf")
    c32.SaveAs("massCiCLowCats.png")



    c4 = ROOT.TCanvas("c4", "c4", 1200, 800)
    if (options.TeV==8):
        c4.Divide(3,2)
    else:
        c4.Divide(2,2)
    stackBDTMass = []
    temp3 = []
    l4 = []
    for c in xrange(len(bdtCategories)-1):
        c4.cd(c+1)
        stackBDTMass.append(ROOT.THStack("s4"+str(c), "s4"+str(c)))
        temp3.append(hBDTMass[1+c*len(groupType)].Clone())
        for i in xrange(1, len(groupType)-1):    
            stackBDTMass[-1].Add(hBDTMass[i+c*len(groupType)])
            if (i != 1):
                hBDTError[1].Add(hBDTError[i+c*len(groupType)])
                temp3[-1].Add(hBDTMass[i+c*len(groupType)])
        stackBDTMass[-1].Draw()
        maximum = stackBDTMass[-1].GetMaximum()*1.3
        if (maximum < 10.):
            maximum = 15
        stackBDTMass[-1].SetMaximum(maximum)
        hBDTMass[c*len(groupType)].Draw("PESAME")
        hBDTMass[len(groupType)-1+c*len(groupType)].Scale(5)
        hBDTMass[len(groupType)-1+c*len(groupType)].Draw("SAME")
        for i in xrange(1, temp3[-1].GetXaxis().GetNbins()+1):
            temp3[-1].SetBinError(i, hBDTError[1+c*len(groupType)].GetBinContent(i))
        temp3[-1].Draw("E2SAME")
        temp3[-1].SetFillColor(ROOT.kBlack)
        temp3[-1].SetFillStyle(3004)
        temp3[-1].SetMarkerStyle(0)
        stackBDTMass[-1].GetXaxis().SetTitle("m_{#gamma#gamma} (GeV)")
        stackBDTMass[-1].GetYaxis().SetTitle("Events/2 GeV")
        stackBDTMass[-1].GetYaxis().SetTitleOffset(1.2)
        txt1 = ROOT.TLatex()
        txt1.SetNDC()
        txt1.SetTextSize(0.05)
        txt1.SetTextAlign(12)
        if (options.TeV == 8):
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=8 TeV L=19.6 fb^{-1}}}")
        else:
            txt1.DrawLatex(0.31, 0.85, "#scale[0.8]{#splitline{CMS Preliminary}{#sqrt{s}=7 TeV L=5.1 fb^{-1}}}")
            
        l4.append(ROOT.TLegend(0.60, 0.65, 0.88, 0.88))
        l4[-1].SetFillColor(ROOT.kWhite)
        l4[-1].SetBorderSize(0)
        l4[-1].AddEntry(hCiCMass[0], "Data", "PE")
        l4[-1].AddEntry(hCiCMass[1], "2 prompt #gamma", "F")
        l4[-1].AddEntry(hCiCMass[2], "1 prompt #gamma 1 fake #gamma", "F")
        l4[-1].AddEntry(hCiCMass[3], "2 fake #gamma", "F")
        l4[-1].AddEntry(hCiCMass[4], "Drell-Yan", "F")
        l4[-1].AddEntry(hCiCMass[5], "H#rightarrow#gamma#gamma(125 GeV) x5", "F")
        l4[-1].Draw("SAME")
        c4.RedrawAxis()
    c4.SaveAs("massBDTCats.pdf")
    c4.SaveAs("massBDTCats.png")

if __name__ == "__main__":
    if (options.TeV == 8):
        groupType = [[0], [3], [12,22,32,42], [11,21], [5], [-125000, -125100, -125400, -125500]]
        kfactors = [[0], [0.15], [0.20,0.20,0.20,0.20], [0.5,0.5], [0.04], [0., 0., 0., 0.]]
        # Jim Categories
        #bdtCategories = [-0.39, 0.13, 0.52, 0.75, 0.915, 1000]
        bdtCategories = [-0.78, -0.42, 0.0, 0.36, 0.76, 1000]
        colors = [0, ROOT.kBlue-8, ROOT.kGreen-9, ROOT.kCyan, ROOT.kMagenta-10, ROOT.kRed]
    else:
        groupType = [[0], [4, 14, 24], [12,22,32], [11,21], [5], [-125000, -125100, -125400, -125500]]
        kfactors = [[0], [0.15, 0.15, 0.15], [0.20,0.20,0.20], [0.5,0.5], [0.04], [0., 0., 0., 0.]]
        # Jim Categories
        #bdtCategories = [0.42, 0.79, 0.93, 0.975, 1000]
        bdtCategories = [0.19, 0.70, 0.85, 0.93, 1000]
        colors = [0, ROOT.kBlue-8, ROOT.kGreen-9, ROOT.kCyan, ROOT.kMagenta-10, ROOT.kRed]

    if (options.eventLooper):
        eventLoop()
    if (options.drawPlot):
        drawPlots()
