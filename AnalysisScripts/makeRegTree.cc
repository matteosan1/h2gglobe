#include "TROOT.h"
#include "TChain.h"
#include "TProof.h"

#include <iostream>
#include <stdlib.h> 

using namespace std;

int main(int argc, char** argv) {
  
  if (argc == 0) {
    std::cout << "You need at least one parameter." << std::endl;
    abort();
  }

  TChain *ch = new TChain("event");

  char const * postfix("");
  int type = atoi(argv[1]);
  if (type == 0) {
    ch->Add("/afs/cern.ch/user/s/sani/eos/cms/store/group/phys_higgs/cmshgg/reduced/HggReduction_forRegression_v7/GJet_Pt-20to40_doubleEMEnriched_TuneZ2star_14TeV-pythia6_GEM2019Upg14DR-Phase1NoAgedJan23_PU50BX25_DES19_62_V8-v1/*.root");
    postfix = "20_40_PI_noAged";
  } else if (type == 1) {
    ch->Add("/afs/cern.ch/user/s/sani/eos/cms/store/group/phys_higgs/cmshgg/reduced/HggReduction_forRegression_v7/GJet_Pt40_doubleEMEnriched_TuneZ2star_14TeV-pythia6_GEM2019Upg14DR-Phase1NoAgedJan23_PU50BX25_DES19_62_V8-v1/*.root");
    postfix = "40_ind_PI_noAged";
  } else if (type == 2) {
    ch->Add("/afs/cern.ch/user/s/sani/eos/cms/store/group/phys_higgs/cmshgg/reduced/HggReduction_forRegression_v7/GJet_Pt-20to40_doubleEMEnriched_TuneZ2star_14TeV-pythia6_GEM2019Upg14DR-Phase1age1kfixJan23_PU140BX25_PH1_1K_FB_V2-v1/*.root");
    postfix = "20_40_PI_1k";
  } else if (type == 3) {
    ch->Add("/afs/cern.ch/user/s/sani/eos/cms/store/group/phys_higgs/cmshgg/reduced/HggReduction_forRegression_v7/GJet_Pt40_doubleEMEnriched_TuneZ2star_14TeV-pythia6_GEM2019Upg14DR-Phase1age1kfixJan23_PU140BX25_PH1_1K_FB_V2-v1/*.root");
    postfix = "40_inf_PI_1k";
  } else if (type == 6) {
    ch->Add("/afs/cern.ch/user/s/sani/eos/cms/store/group/phys_higgs/cmshgg/reduced/HggReduction_forRegression_v8/GluGluToHToGG_M-125_14TeV-powheg-pythia6_GEM2019Upg14DR-Phase1age1kfixJan23_PU140BX25_PH1_1K_FB_V2-v1/*.root");
    postfix = "HGG_PI_1k";
  }
  TProof* p = TProof::Open("lite://");
  p->SetParallel(10);
  
  ch->SetProof();

  cout<<"Start analyzing the chain ..."<<endl;

  ch->Process("RegressionTreeMaker2.C+", postfix);
  //gProof->GetOutputList()->ls();
  // also "+" suffix is always recommended:
  // ch->Process("OccAnalysis.C+");

  cout<<" ... analyzing the chain completed"<<endl;
  cout<<" ... writing output done "<<endl;
}
