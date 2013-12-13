import ROOT
import math, array
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--data", default="histograms_CMS-HGG_zeevalidation.root", help="Input file for data. \Default: %default")
parser.add_option("-m", "--mc", default="histograms_CMS-HGG_zeevalidation_david_template_envelopes.root", help="Input file for MC. \Default: %default")
parser.add_option("-p", "--passMva", default=False, action="store_true", help="Select events passing diphoton MVA min cut.")
parser.add_option("-n", "--normalize", default=True, action="store_true", help="Normalize to same area")
parser.add_option("-t", "--TeV", default=8, help="Setup for 7TeV data")
(options, arg) = parser.parse_args()

ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetOptStat(0)

ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetFrameBorderMode(0)

ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetLineColor(1)

legends = []
ratio = []
ratio_syst = []
ratio_syst_up = []
ratio_syst_down = []
hist_syst = []
hist_syst_up = []
hist_syst_down = []
mc_temp = []
graphs = []
ratio_graphs= []

def plotRatio(cat, data, mc, mc_top1, mc_bottom1, mc_top2, mc_bottom2, passMVAcut, equalArea):
    global ratio, ratio_syst, ratio_syst_up, ratio_syst_down
    global ratio_graphs

    ratio_syst.append(mc_bottom1[cat].Clone())
    ratio_syst[-1].Add(mc_top1[cat].Clone())
    ratio_syst[-1].Add(mc_bottom2[cat].Clone())
    ratio_syst[-1].Add(mc_top2[cat].Clone())
    ratio_syst[-1].Scale(0.25)
    x = array.array('f', [])
    y = array.array('f', [])
    eyu = array.array('f', [])
    eyd = array.array('f', [])
    exu = array.array('f', [])
    exd = array.array('f', [])

    ratio_syst_up.append(ratio_syst[-1].Clone())
    ratio_syst_down.append(ratio_syst[-1].Clone())
    
    for i in xrange(1, ratio_syst[-1].GetNbinsX()+1):
        up   = math.sqrt(math.pow(mc_top1[cat].GetBinContent(i)-mc[cat].GetBinContent(i),2)+math.pow(mc_top2[cat].GetBinContent(i)-mc[cat].GetBinContent(i),2));
        down = math.sqrt(math.pow(mc_bottom1[cat].GetBinContent(i)-mc[cat].GetBinContent(i),2)+math.pow(mc_bottom2[cat].GetBinContent(i)-mc[cat].GetBinContent(i),2));

        x.append(ratio_syst[-1].GetXaxis().GetBinCenter(i))
        y.append(ratio_syst[-1].GetBinContent(i))
        eyu.append(up)
        eyd.append(down)
        exu.append(0)
        exd.append(0)
        ratio_syst_up[-1].SetBinContent(i, ratio_syst[-1].GetBinContent(i)+up);
        ratio_syst_down[-1].SetBinContent(i, ratio_syst[-1].GetBinContent(i)-down);
    
    sf = 1
    if (passMVAcut):
        sf = data[cat].Integral(48,100)/mc[cat].Integral(48,100)
    else:
        sf = data[cat].Integral()/mc[cat].Integral()
    if (not equalArea):
        sf = data[0].Integral()/mc[0].Integral()

    mc[cat].Scale(sf)
    ratio_syst_up[-1].Scale(sf)
    ratio_syst_down[-1].Scale(sf)

    for i in xrange(hist_syst[-1].GetNbinsX()):
        if (mc[cat].GetBinContent(i+1) !=0):
            y[i] = y[i]*sf/mc[cat].GetBinContent(i+1)
            eyd[i] = eyd[i]*sf/mc[cat].GetBinContent(i+1)
            eyu[i] = eyu[i]*sf/mc[cat].GetBinContent(i+1)
        else:
            y[i] = 0

    ratio.append(data[cat].Clone())
    ratio[-1].Divide(mc[cat])
    ratio_syst[-1].Divide(mc[cat])
    ratio_syst_up[-1].Divide(mc[cat])
    ratio_syst_down[-1].Divide(mc[cat])

    ratio[-1].Draw("e")
    ratio[-1].GetYaxis().SetRangeUser(0.2, 1.8)
    ratio_graphs.append(ROOT.TGraphAsymmErrors(len(x), x, y, exd, exu, eyd, eyu))
    ratio_graphs[-1].SetFillStyle(3013)
    ratio_graphs[-1].SetFillColor(ROOT.kRed)
    ratio_graphs[-1].Draw("e3,same")
    ratio_syst_up[-1].SetLineColor(ROOT.kRed)
    ratio_syst_down[-1].SetLineColor(2)
    ratio_syst_up[-1].SetFillStyle(0)
    ratio_syst_down[-1].SetFillStyle(0)
    ratio_syst_up[-1].Draw("hist,same")
    ratio_syst_down[-1].Draw("hist,same")
    ratio[-1].Draw("e,same")
    ROOT.gPad.SetGridx()
    ROOT.gPad.SetGridy()
    ROOT.gPad.RedrawAxis()
    

def plotDataMC(cat, data, mc, mc_top1, mc_bottom1, mc_top2, mc_bottom2, passMVAcut, equalArea):
    global hist_syst, hist_syst_up, hist_syst_down, mc_temp
    global graphs

    mc_temp.append(mc[cat].Clone())
    hist_syst.append(mc_bottom1[cat].Clone())
    hist_syst[-1].Add(mc_top1[cat].Clone())
    hist_syst[-1].Add(mc_bottom2[cat].Clone())
    hist_syst[-1].Add(mc_top2[cat].Clone())
    hist_syst[-1].Scale(0.25)
    x = array.array('f', [])
    y = array.array('f', [])
    eyu = array.array('f', [])
    eyd = array.array('f', [])
    exu = array.array('f', [])
    exd = array.array('f', [])

    hist_syst_up.append(hist_syst[-1].Clone())
    hist_syst_down.append(hist_syst[-1].Clone())
    
    for i in xrange(1, hist_syst[-1].GetNbinsX()+1):
        up   = math.sqrt(math.pow(mc_top1[cat].GetBinContent(i)-mc_temp[-1].GetBinContent(i),2)+math.pow(mc_top2[cat].GetBinContent(i)-mc_temp[-1].GetBinContent(i),2));
        down = math.sqrt(math.pow(mc_bottom1[cat].GetBinContent(i)-mc_temp[-1].GetBinContent(i),2)+math.pow(mc_bottom2[cat].GetBinContent(i)-mc_temp[-1].GetBinContent(i),2));

        x.append(hist_syst[-1].GetXaxis().GetBinCenter(i))
        y.append(hist_syst[-1].GetBinContent(i))
        eyu.append(up)
        eyd.append(down)
        exu.append(0)
        exd.append(0)
        hist_syst_up[-1].SetBinContent(i, hist_syst[-1].GetBinContent(i)+up);
        hist_syst_down[-1].SetBinContent(i, hist_syst[-1].GetBinContent(i)-down);
  
    sf = 1
    if (passMVAcut):
        sf = data[cat].Integral(48,100)/mc_temp[-1].Integral(48,100)
    else:
        sf = data[cat].Integral()/mc_temp[-1].Integral()
    if (not equalArea):
        sf = data[0].Integral()/mc[0].Integral()
        
    mc_temp[-1].Scale(sf)
    hist_syst_up[-1].Scale(sf)
    hist_syst_down[-1].Scale(sf)

    for i in xrange(hist_syst[-1].GetNbinsX()):
        y[i] = y[i]*sf
    graphs.append(ROOT.TGraphAsymmErrors(len(x), x, y, exd, exu, eyd, eyu))
    graphs[-1].SetFillStyle(3013)
    graphs[-1].SetFillColor(ROOT.kRed)
    legends.append(ROOT.TLegend(.6,.65,.87,.87))
    legends[-1].SetBorderSize(0);
    legends[-1].SetFillColor(10);
    legends[-1].SetTextSize(.035);
    legends[-1].AddEntry(data[0],"Data 8TeV (19.6fb^{-1})");
    legends[-1].AddEntry(mc_temp[-1],"DYJetsToLL MC","F");
    legends[-1].AddEntry(graphs[-1],"MC with idmva #pm 0.01", "F");
    legends[-1].AddEntry(0, "and #sigma_{E} s.f. 10%","");
    data[cat].Draw("pe")
    legends[-1].Draw("same")
    data[cat].SetMaximum(data[cat].GetMaximum()*1.3)
    data[cat].GetXaxis().SetTitle("BDT Output")
    mc_temp[-1].Draw("hist,same")
    graphs[-1].Draw("e3,same")
    hist_syst_up[-1].SetLineColor(ROOT.kRed)
    hist_syst_down[-1].SetLineColor(2)
    hist_syst_up[-1].SetFillStyle(0)
    hist_syst_down[-1].SetFillStyle(0)
    hist_syst_up[-1].Draw("hist,same")
    hist_syst_down[-1].Draw("hist,same")
    data[cat].Draw("pe,same")
    ROOT.gPad.RedrawAxis()


fMC = ROOT.TFile(options.mc)
fData   = ROOT.TFile(options.data)
data = []
mc = []
mc_top1 = []
mc_top2 = []
mc_bottom1 = []
mc_bottom2 = []

for i in xrange(5):
    fData.cd()
    data.append(fData.Get("bdtout_cat"+str(i)+"_Data"))
    data[-1].Rebin(2)
    data[-1].SetMarkerStyle(20)
    data[-1].SetMarkerSize(0.5)
    fMC.cd()
    mc.append(fMC.Get("bdtout_cat"+str(i)+"_DYJetsToLL"))
    mc[-1].Rebin(2)
    mc[-1].SetFillColor(38)
    mc_top1.append(fMC.Get("bdtout_cat"+str(i)+"_DYJetsToLL_top"))
    mc_top1[-1].Rebin(2)
    mc_top2.append(fMC.Get("bdtout_sigmaE_cat"+str(i)+"_DYJetsToLL_top"))
    mc_top2[-1].Rebin(2)
    mc_bottom1.append(fMC.Get("bdtout_cat"+str(i)+"_DYJetsToLL_bottom"))
    mc_bottom1[-1].Rebin(2)
    mc_bottom2.append(fMC.Get("bdtout_sigmaE_cat"+str(i)+"_DYJetsToLL_bottom"))
    mc_bottom2[-1].Rebin(2)

c_bdtout = ROOT.TCanvas("c_bdtout","BDT output",2200,800)
c_bdtout.Divide(4,2);

for i in xrange(1,5):
    c_bdtout.cd(i)
    plotDataMC(i, data, mc, mc_top1, mc_bottom1, mc_top2, mc_bottom2, False, True)
    c_bdtout.cd(i+4)
    plotRatio(i, data, mc, mc_top1, mc_bottom1, mc_top2, mc_bottom2, False, True)

if (options.TeV == 7):
    c_bdtout.SaveAs("bdtout_basecat_syst_7TeV.png")
else:
    c_bdtout.SaveAs("bdtout_basecat_syst.png")

data = []
mc = []
mc_top1 = []
mc_top2 = []
mc_bottom1 = []
mc_bottom2 = []

suffix  = ["_cat0", "EB_cat0", "EBEE_cat0", "EE_cat0"]
suffix2 = ["_sigmaE_cat0", "EB_sigmaE_cat0", "EBEE_sigmaE_cat0", "EE_sigmaE_cat0"]

for i in xrange(4):
    fData.cd()
    data.append(fData.Get("bdtout"+suffix[i]+"_Data"))
    data[-1].Rebin(2)
    data[-1].SetMarkerStyle(20)
    data[-1].SetMarkerSize(0.5)
    fMC.cd()
    mc.append(fMC.Get("bdtout"+suffix[i]+"_DYJetsToLL"))
    mc[-1].Rebin(2)
    mc[-1].SetFillColor(38)
    mc_top1.append(fMC.Get("bdtout"+suffix[i]+"_DYJetsToLL_top"))
    mc_top1[-1].Rebin(2)
    mc_top2.append(fMC.Get("bdtout"+suffix2[i]+"_DYJetsToLL_top"))
    mc_top2[-1].Rebin(2)
    mc_bottom1.append(fMC.Get("bdtout"+suffix[i]+"_DYJetsToLL_bottom"))
    mc_bottom1[-1].Rebin(2)
    mc_bottom2.append(fMC.Get("bdtout"+suffix2[i]+"_DYJetsToLL_bottom"))
    mc_bottom2[-1].Rebin(2)

c_bdtout2 = ROOT.TCanvas("c_bdtout2","BDT output",2200,800)
c_bdtout2.Divide(4,2);

for i in xrange(0,4):
    c_bdtout2.cd(i+1)
    plotDataMC(i, data, mc, mc_top1, mc_bottom1, mc_top2, mc_bottom2, False, True)
    c_bdtout2.cd(i+5)
    plotRatio(i, data, mc, mc_top1, mc_bottom1, mc_top2, mc_bottom2, False, True)

if (options.TeV == 7):
    c_bdtout2.SaveAs("bdtout_syst_7TeV.png")
else:
    c_bdtout2.SaveAs("bdtout_syst.png")
