import ROOT
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--TeV", default=8, help="Setup for 7 or 8 TeV")
parser.add_option("-i", "--inputfile", help="Input file for the macro.")

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetPalette(1)

appendix = "_8TeV"
cats = 5
if (options.TeV == 7):
    cats = 4
    appendix = "_7TeV"

hptgg = []
hminr9 = []
hmaxeta = []
h2d = []
h2dEta = []

#colors = []
#colors.append(ROOT.gROOT.GetColor(ROOT.ROOT.kRed))
#colors[-1].SetAlpha(0.5)
#colors.append(ROOT.gROOT.GetColor(ROOT.ROOT.kYellow))
#colors[-1].SetAlpha(0.5)
#colors.append(ROOT.gROOT.GetColor(ROOT.ROOT.kGreen))
#colors[-1].SetAlpha(0.5)
#colors.append(ROOT.gROOT.GetColor(ROOT.ROOT.kBlue))
#colors[-1].SetAlpha(0.5)
#colors.append(ROOT.gROOT.GetColor(ROOT.ROOT.kViolet))
#colors[-1].SetAlpha(0.5)
colors = [ROOT.ROOT.kRed, ROOT.kYellow, ROOT.kGreen, ROOT.kBlue, ROOT.kViolet]

for i in xrange(cats):
    hptgg.append(ROOT.TH1F("ptgg"+str(i), "", 100, 0, 500))
    hptgg[-1].SetFillColor(colors[i])
    hminr9.append(ROOT.TH1F("minr9"+str(i), "", 100, 0.5, 1))
    hminr9[-1].SetFillColor(colors[i])
    hmaxeta.append(ROOT.TH1F("maxeta"+str(i), "", 25, 0, 2.5))
    hmaxeta[-1].SetLineColor(colors[i])
    hmaxeta[-1].SetFillColor(colors[i])
    hmaxeta[-1].SetFillStyle(3002)
    h2d.append(ROOT.TH2F("h2d"+str(i),"h2d"+str(i), 25, 0, 2.5, 100, 0.5, 1))
    h2dEta.append(ROOT.TH2F("h2dEta"+str(i),"h2dEta"+str(i), 50, -2.5, 2.5, 50, -2.5, 2.5))
    
f = ROOT.TFile(options.inputfile)
t = f.Get("opttree")

entries = t.GetEntries()

for z in xrange(entries):
    t.GetEntry(z)

    if (t.itype < -124999 and t.itype > -125999):
        if (t.full_cat < cats):
            hptgg[int(t.full_cat)].Fill(t.dipho_pt, t.full_weight)
            hminr9[int(t.full_cat)].Fill(min(t.r91, t.r92), t.full_weight)
            hmaxeta[int(t.full_cat)].Fill(max(abs(t.eta1), abs(t.eta2)), t.full_weight)
            h2d[int(t.full_cat)].Fill(max(abs(t.eta1), abs(t.eta2)), min(t.r91, t.r92), t.full_weight)
            h2dEta[int(t.full_cat)].Fill((t.eta1), (t.eta2), t.full_weight)
            
c1 = ROOT.TCanvas("c1", "c1")
for i in xrange(cats):
    hptgg[i].Scale(1./hptgg[i].Integral())
for i in xrange(cats-1, -1, -1):
    if (i == cats-1):
        hptgg[i].Draw()
        hptgg[i].SetMaximum(0.175)
        hptgg[i].GetXaxis().SetTitle("p_{T}(#gamma#gamma) (GeV)")
    else:
        hptgg[i].Draw("SAME")
l = ROOT.TLegend(0.5, 0.6, 0.88, 0.88)
l.SetBorderSize(0)
l.SetFillColor(ROOT.kWhite)
l.SetHeader("CMS Simulation")
l.AddEntry(hptgg[0], "untagged 0", "F")
l.AddEntry(hptgg[1], "untagged 1", "F")
l.AddEntry(hptgg[2], "untagged 2", "F")
l.AddEntry(hptgg[3], "untagged 3", "F")
if (options.TeV == 8):
    l.AddEntry(hptgg[4], "untagged 4", "F")
    l.SetHeader("MC Signal (m_{H}=125GeV, #sqrt{s}=8TeV)")
else:    
    l.SetHeader("MC Signal (m_{H}=125GeV, #sqrt{s}=7TeV)")
l.Draw("SAME")

c1.SaveAs("hptgg_untagged_cats"+appendix+".png")

c2 = ROOT.TCanvas("c2", "c2")
c2.SetLogy(1)
for i in xrange(cats):
    hminr9[i].Scale(1./hminr9[i].Integral())
    
for i in xrange(cats-1, -1, -1):
    if (i == cats-1):
        hminr9[i].Draw()
        hminr9[i].SetMaximum(0.5)       
        hminr9[i].SetMinimum(1e-3)
        hminr9[i].GetXaxis().SetTitleOffset(1.2)
        hminr9[i].GetXaxis().SetTitle("min(R9_{#gamma1}, R9_{#gamma2})")
    else:
        hminr9[i].Draw("SAME")
l1 = ROOT.TLegend(0.1, 0.6, 0.5, 0.88)
l1.SetBorderSize(0)
l1.SetFillColor(ROOT.kWhite)
l1.AddEntry(hminr9[0], "untagged 0", "F")
l1.AddEntry(hminr9[1], "untagged 1", "F")
l1.AddEntry(hminr9[2], "untagged 2", "F")
l1.AddEntry(hminr9[3], "untagged 3", "F")
if (options.TeV == 8):
    l1.AddEntry(hminr9[4], "untagged 4", "F")
    l1.SetHeader("MC Signal (m_{H}=125GeV, #sqrt{s}=8TeV)")
else:    
    l1.SetHeader("MC Signal (m_{H}=125GeV, #sqrt{s}=7TeV)")
l1.Draw("SAME")        
c2.SaveAs("hminr9_untagged_cats"+appendix+".png")

c3 = ROOT.TCanvas("c3", "c3")
for i in xrange(cats):
    hmaxeta[i].Scale(1./hmaxeta[i].Integral())
for i in xrange(cats-1, -1, -1):    
    if (i == cats-1):
        hmaxeta[i].Draw()
        hmaxeta[i].SetMaximum(0.2)
        hmaxeta[i].GetXaxis().SetTitle("|#eta|")
    else:
        hmaxeta[i].Draw("SAME")
l2 = ROOT.TLegend(0.5, 0.6, 0.88, 0.88)
l2.SetBorderSize(0)
l2.SetFillColor(ROOT.kWhite)
l2.AddEntry(hmaxeta[0], "untagged 0", "F")
l2.AddEntry(hmaxeta[1], "untagged 1", "F")
l2.AddEntry(hmaxeta[2], "untagged 2", "F")
l2.AddEntry(hmaxeta[3], "untagged 3", "F")
if (options.TeV == 8):
    l2.AddEntry(hmaxeta[4], "untagged 4", "F")
    l2.SetHeader("MC Signal (m_{H}=125GeV, #sqrt{s}=8TeV)")
else:    
    l2.SetHeader("MC Signal (m_{H}=125GeV, #sqrt{s}=7TeV)")
l2.Draw("SAME")        
c3.SaveAs("hmaxeta_untagged_cats"+appendix+".png")

line1 = []
line2 = []
c4 = ROOT.TCanvas("c4", "c4", 800*cats, 800)
c4.Divide(cats, 1)
for i in xrange(cats):
    c4.cd(i+1)
    h2d[i].Draw("COLZ")
    h2d[i].GetXaxis().SetTitle("max(|#eta|)")
    h2d[i].GetYaxis().SetTitleOffset(1.4)
    h2d[i].GetYaxis().SetTitle("min(R9)")
    line1.append(ROOT.TLine(1.5, 0.5, 1.5, 1))
    line2.append(ROOT.TLine(0, 0.94, 2.5, 0.94))
    line1[-1].Draw("SAME")
    line2[-1].Draw("SAME")
c4.SaveAs("h2Dmaxeta_minr9_untagged_cats"+appendix+".png")


c5 = ROOT.TCanvas("c5", "c5", 800*cats, 800)
c5.Divide(cats, 1)
for i in xrange(cats):
    c5.cd(i+1)
    h2dEta[i].Draw("COLZ")
    h2dEta[i].GetXaxis().SetTitle("lead |#eta|")
    h2dEta[i].GetYaxis().SetTitle("sublead |#eta|")
    h2dEta[i].GetYaxis().SetTitleOffset(1.4)
c5.SaveAs("h2Deta_untagged_cats"+appendix+".png")        

