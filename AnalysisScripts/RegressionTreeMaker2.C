#define RegressionTreeMaker2_cxx
// The class definition in RegressionTreeMaker2.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.

// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// Root > T->Process("RegressionTreeMaker2.C")
// Root > T->Process("RegressionTreeMaker2.C","some options")
// Root > T->Process("RegressionTreeMaker2.C+")
//

#include "RegressionTreeMaker2.h"
#include <TH2.h>
#include <TStyle.h>
#include <iostream>
#include <TLorentzVector.h>

void RegressionTreeMaker2::Begin(TTree * /*tree*/)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();
   std::cout << "Producing ntuple for: " << option.Data() << std::endl;
   TString dirname("/tmp/sani/regressionTree_");
   outFile = new TFile(dirname+option.Data()+TString(".root"), "RECREATE");

}

void RegressionTreeMaker2::SlaveBegin(TTree * /*tree*/)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

   outTree = new TTree("regressionTree","regressionTree");

   outTree->Branch("evt", &evt, "evt/I");
   outTree->Branch("sieie_pho",&sieie_pho,"sieie_pho/F");
   outTree->Branch("sieip_pho",&sieip_pho,"sieip_pho/F");
   outTree->Branch("r9_pho",&r9_pho,"r9_pho/F");
   outTree->Branch("E2byE5_pho", &E2byE5_pho, "E2byE5_pho/F");
   //   outTree->Branch("pf_pho_iso",&pf_pho_iso,"pf_pho_iso/F");
   //   outTree->Branch("pf_charged_iso_chosenvtx",&pf_charged_iso_chosenvtx,"pf_charged_iso_chosenvtx/F");
   //   outTree->Branch("pf_charged_iso_badvtx",&pf_charged_iso_badvtx,"pf_charged_iso_badvtx/F");
   outTree->Branch("rho",&rho,"rho/F");
   outTree->Branch("sc_eta_pho",&sc_eta_pho,"sc_eta_pho/F");
   outTree->Branch("sc_phi_pho",&sc_phi_pho,"sc_phi_pho/F");
   outTree->Branch("scRaw_pho",&scRaw_pho,"scRaw_pho/F");
   outTree->Branch("genenergy_pho",&genenergy_pho,"genenergy_pho/F");
   outTree->Branch("genmatched_pho",&genmatched_pho,"genmatched_pho/I");
   outTree->Branch("isbarrel_pho",&isbarrel_pho,"isbarrel_pho/I");

   outTree->Branch("tgtvar",&tgtvar,"tgtvar/F");
   outTree->Branch("seedOverRaw",&seedOverRaw,"seedOverRaw/F");

   outTree->Branch("pho_sc_seta",&pho_sc_seta,"pho_sc_seta/F");
   outTree->Branch("pho_sc_sphi",&pho_sc_sphi,"pho_sc_sphi/F");
   outTree->Branch("pho_sc_nbc",&pho_sc_nbc,"pho_sc_nbc/F"); // int?                                                                              
   outTree->Branch("hoe_pho",&hoe_pho,"_hoe_pho/F");
   outTree->Branch("pho_vtx_std_n",&pho_vtx_std_n,"pho_vtx_std_n/F"); // int?         
   
   outTree->Branch("bc_sc_deta",&bc_sc_deta,"bc_sc_deta/F");
   outTree->Branch("bc_sc_dphi",&bc_sc_dphi,"bc_sc_dphi/F");
   //outTree->Branch("be3x3_be5x5",&be3x3_be5x5,"be3x3_be5x5/F");
   //outTree->Branch("pho_sipip_sqrt",&pho_sipip_sqrt,"pho_sipip_sqrt/F"); // sqrt                                         
   //outTree->Branch("bemax_be5x5",&bemax_be5x5,"bemax_be5x5/F");
   //outTree->Branch("be2nd_be5x5",&be2nd_be5x5,"be2nd_be5x5/F");
   //outTree->Branch("betop_be5x5",&betop_be5x5,"betop_be5x5/F");
   //outTree->Branch("bebottom_be5x5",&bebottom_be5x5,"bebottom_be5x5/F");
   //outTree->Branch("beleft_be5x5",&beleft_be5x5,"beleft_be5x5/F");
   //outTree->Branch("beright_be5x5",&beright_be5x5,"beright_be5x5/F");
   //outTree->Branch("be2x5max_be5x5",&be2x5max_be5x5,"be2x5max_be5x5/F");
   //outTree->Branch("be2x5top_be5x5",&be2x5top_be5x5,"be2x5top_be5x5/F");
   //outTree->Branch("be2x5bottom_be5x5",&be2x5bottom_be5x5,"be2x5bottom_be5x5/F");
   //outTree->Branch("be2x5left_be5x5",&be2x5left_be5x5,"be2x5left_be5x5/F");
   //outTree->Branch("be2x5right_be5x5",&be2x5right_be5x5,"be2x5right_be5x5");
   
   outTree->Branch("be3x3_be5x5",&be3x3_be5x5,"be3x3_be5x5/F");
   outTree->Branch("sipip_pho",&pho_sipip_sqrt,"sipip_pho/F");
   outTree->Branch("bemax_be5x5",&bemax_be5x5,"bemax_be5x5/F");
   outTree->Branch("be2nd_be5x5",&be2nd_be5x5,"be2nd_be5x5/F");
   outTree->Branch("betop_be5x5",&betop_be5x5,"betop_be5x5/F");
   outTree->Branch("bebottom_be5x5",&bebottom_be5x5,"bebottom_be5x5/F");
   outTree->Branch("beleft_be5x5",&beleft_be5x5,"beleft_be5x5/F");
   outTree->Branch("beright_be5x5",&beright_be5x5,"beright_be5x5/F");
   outTree->Branch("be2x5max_be5x5",&be2x5max_be5x5,"be2x5max_be5x5/F");
   outTree->Branch("be2x5top_be5x5",&be2x5top_be5x5,"be2x5top_be5x5/F");
   outTree->Branch("be2x5bottom_be5x5",&be2x5bottom_be5x5,"be2x5bottom_be5x5/F");
   outTree->Branch("be2x5left_be5x5",&be2x5left_be5x5,"be2x5left_be5x5/F");
   outTree->Branch("be2x5right_be5x5",&be2x5right_be5x5,"be2x5right_be5x5/F");
   outTree->Branch("be5x5_eseed", &be5x5_eseed, "be5x5_eseed/F");
   outTree->Branch("bieta_pho", &bieta_pho, "bieta_pho/I");
   outTree->Branch("biphi_pho", &biphi_pho, "biphi_pho/I");
   outTree->Branch("betacry_pho", &betacry_pho, "betacry_pho/F");
   outTree->Branch("bieta_var1", &bieta_var1, "bieta_var1/I");
   outTree->Branch("biphi_var1", &biphi_var1, "biphi_var1/I");
   outTree->Branch("bi_var2", &bi_var2, "bi_var2/I");
   outTree->Branch("biphi_var2", &biphi_var2, "biphi_var2/I");
   outTree->Branch("bphicry_pho", &bphicry_pho, "&bphicry_pho/F");

   //outTree->Branch("pre",&pre,"pre/F"); // endcp only 
 
   fOutput->Add(outTree);
}

Bool_t RegressionTreeMaker2::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // It can be passed to either RegressionTreeMaker2::GetEntry() or TBranch::GetEntry()
   // to read either all or the required parts of the data. When processing
   // keyed objects with PROOF, the object is already loaded and is available
   // via the fObject pointer.
   //
   // This function should contain the "body" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.
   //
   // The processing can be stopped by calling Abort().
   //
   // Use fStatus to set the return value of TTree::Process().
   //
   // The return value is currently not used.

  std::map<int,std::string> bad;
  //  bad[6614] = std::string("2_2.root");
  //  bad[6954] = std::string("2_6.root");

  if (bad.count(entry)) {
    const TFile *current_file = ((TChain*)(fChain))->GetCurrentFile();
    if (current_file) {
      const char *current_file_name = current_file->GetName();
      if (current_file_name) {
        if (strstr(current_file_name,bad[entry].c_str())) {
          return kFALSE;
        } else {
	  std::cout << " Bad entry number " << entry << " but not the right file (current_file_name=" << current_file_name <<"), continuing..." << std::endl;
        }
      } else {
	std::cout << " Could not get current_file_name" << std::endl;
      }
    } else {
      std::cout << " Could not get current_file" << std::endl;
    }
  }

  //std::cout << " before GetEntry(" << entry << ")" << std::endl;
  GetEntry(entry);
  //std::cout << " after GetEntry(" << entry << ")" << std::endl;

  //std::cout << "SCZ: " << pho_n << std::endl;
  for (int i = 0 ; i < pho_n ; i++) {
    TLorentzVector *phop4 = (TLorentzVector*)(pho_p4->At(i));
    if (!phop4) {
      //std::cout << "Photon " << i << "/" << pho_n << " seems to be null?" << std::endl;
    } else {

      if (pho_genmatched[i] && pho_genenergy[i] > 20. 
          && fabs(phop4->Eta()) < 2.5 && !(fabs(phop4->Eta()) > 1.4442 && fabs(phop4->Eta()) < 1.556)) {

	TLorentzVector *bcpos =(TLorentzVector*)bc_p4->At(sc_bcseedind[pho_scind[i]]);
	TVector3 *scpos = (TVector3*)sc_xyz->At(pho_scind[i]);

	evt = event;
        sieie_pho = pho_sieie[i];
        sieip_pho = pho_sieip[i];
        //E2byE5_pho = bc_s25[sc_bcseedind[pho_scind[i]]] > 0. ? pho_e2x2[i]/bc_s25[sc_bcseedind[pho_scind[i]]] : 99.;
        E2byE5_pho = pho_e2x2[i]/pho_e5x5[i];
        r9_pho = pho_r9[i];
        rho = rho_algo1;
        sc_eta_pho = scpos->Eta();
        sc_phi_pho = scpos->Phi();
        scRaw_pho = sc_raw[pho_scind[i]];
        genenergy_pho = pho_genenergy[i];
	genmatched_pho = pho_genmatched[i];
	isbarrel_pho = (fabs(phop4->Eta()) < 1.4442);
        tgtvar = genenergy_pho/scRaw_pho;
	
	pho_sc_seta = sc_seta[pho_scind[i]];
	pho_sc_sphi = sc_sphi[pho_scind[i]];
	pho_sc_nbc = (float)sc_nbc[pho_scind[i]];
	pho_pho_hoe_bc = pho_hoe_bc[i];
	pho_vtx_std_n = (float)vtx_std_n;
	bc_sc_deta = bcpos->Eta() - scpos->Eta();
	bc_sc_dphi = bcpos->Vect().DeltaPhi(*scpos);
	
	pho_sipip_sqrt = TMath::Sqrt(pho_sipip[i]);
	
	hoe_pho = pho_hoe_bc[i];
	
	bemax_be5x5 = pho_emaxxtal[i]/pho_e5x5[i];
	be2nd_be5x5 = pho_e2nd[i]/pho_e5x5[i];
	betop_be5x5 = pho_etop[i]/pho_e5x5[i];
	bebottom_be5x5 = pho_ebottom[i]/pho_e5x5[i];
	beleft_be5x5 = pho_eleft[i]/pho_e5x5[i];
	beright_be5x5 = pho_eright[i]/pho_e5x5[i];
	be3x3_be5x5 = pho_e3x3[i]/pho_e5x5[i];
	be2x5max_be5x5 = pho_e2x5max[i]/pho_e5x5[i];
	be2x5top_be5x5 = pho_e2x5top[i]/pho_e5x5[i];
	be2x5bottom_be5x5 = pho_e2x5bottom[i]/pho_e5x5[i];
	be2x5left_be5x5 = pho_e2x5left[i]/pho_e5x5[i];
	be2x5right_be5x5 = pho_e2x5right[i]/pho_e5x5[i];
	be5x5_eseed = pho_e5x5[i]/bcpos->E();
	//if ( be5x5_eseed  > 100000.) {
	//  std::cout << pho_e5x5[i] << " " << bcpos->E() << " " << be5x5_eseed << std::endl;
	//  be5x5_eseed = 100000.;
	//}
	seedOverRaw = bcpos->E()/sc_raw[pho_scind[i]];
	
	bieta_pho = pho_bieta[i];
	biphi_pho = pho_biphi[i];
	betacry_pho = pho_betacry[i];
	bieta_var1 = (pho_bieta[i]-1*abs(pho_bieta[i])/pho_bieta[i])%5;
	biphi_var1 = (pho_biphi[i]-1)%2;
	bi_var2 = (abs(pho_bieta[i])<=25)*((pho_bieta[i]-1*abs(pho_bieta[i])/pho_bieta[i])%25) + (abs(pho_bieta[i])>25)*((pho_bieta[i]-26*abs(pho_bieta[i])/pho_bieta[i])%20);
	biphi_var2 = (pho_biphi[i]-1)%20;
	bphicry_pho = pho_bphicry[i];
   
	//pre = sc_pre[pho_scind[i]]/sc_raw[pho_scind[i]];

	//std::cout << be2nd << " " << betop << " " << bebottom << " " << beleft << " " << beright << " " << be2x5max << " " << be2x5top << " " << be2x5bottom 
	//	  << " " << be2x5left << " " << be2x5right << " " << pre << std::endl;

        outTree->Fill();
      }
    }
  }

   return kTRUE;
}

void RegressionTreeMaker2::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.

}

void RegressionTreeMaker2::Terminate()
{
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.

  outTree = dynamic_cast<TTree*>(fOutput->FindObject("regressionTree"));
  //if (outTree) {
  outFile->cd();
  outTree->Write();
  outFile->Close();
  //}
    
}
