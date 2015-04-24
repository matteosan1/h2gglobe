//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Jan 12 17:31:27 2015 by ROOT version 5.34/18
// from TTree event/Reduced tree
// found on file: /afs/cern.ch/work/s/sethzenz/GJ_v8/1_1.root
//////////////////////////////////////////////////////////

#ifndef RegressionTreeMaker2_h
#define RegressionTreeMaker2_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include <TClonesArray.h>

// Fixed size dimensions of array or collections stored in the TTree if any.

class RegressionTreeMaker2 : public TSelector {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   TTree *outTree;
   TFile *outFile;

   Int_t evt;
   float sieie_pho;
   float sieip_pho;
   float r9_pho;
   float E2byE5_pho;
   float etawidth_pho;
   float phiwidth_pho;
   //   float pf_pho_iso;
   //   float pf_charged_iso_chosenvtx;
   //   float pf_charged_iso_badvtx;
   float rho;
   float sc_eta_pho;
   float scRaw_pho;
   float genenergy_pho;
   int isbarrel_pho;
   int genmatched_pho;
   float tgtvar;
   float sc_phi_pho;

   float pho_sc_seta;
   float pho_sc_sphi;
   float pho_sc_nbc; // int?                                                                                                                                                             
   float pho_pho_hoe_bc;
   float pho_vtx_std_n; // int?                                                                                                                                                          

   float bc_sc_deta;
   float bc_sc_dphi;
   float be3x3_be5x5;
   float pho_sipip_sqrt; // sqrt                                                                                                                                                     
   float bemax_be5x5;
   float be2nd_be5x5;
   float betop_be5x5;
   float bebottom_be5x5;
   float beleft_be5x5;
   float beright_be5x5;
   float be2x5max_be5x5;
   float be2x5top_be5x5;
   float be2x5bottom_be5x5;
   float be2x5left_be5x5;
   float be2x5right_be5x5;
   Float_t be5x5_eseed;
   Int_t bieta_pho;
   Int_t biphi_pho;
   Float_t betacry_pho;
   Int_t bieta_var1;
   Int_t biphi_var1;
   Int_t bi_var2;
   Int_t biphi_var2;
   Float_t bphicry_pho;
   float hoe_pho;
   float seedOverRaw;
   float pre; // endcp only                                                                                                                                                          
   // Declaration of leaf types
   TClonesArray    *sc_xyz;
   Int_t          event;
   Int_t           sc_n;
   Float_t         sc_sphi[306];   //[sc_n]
   Float_t         sc_seta[306];   //[sc_n]
   Float_t         sc_raw[306];   //[sc_n]
   Float_t         sc_pre[306];   //[sc_n]
   Int_t           sc_bcseedind[306];   //[sc_n]
   Int_t           sc_nbc[306];   //[sc_n]
   Int_t           bc_n;
   TClonesArray    *bc_p4;
   Float_t         bc_s25[1439];   //[bc_n]
   Int_t           pho_n;
   Float_t         pho_sieie[100];   //[pho_n]
   Float_t         pho_sieip[100];   //[pho_n]
   Float_t         pho_sipip[100];   //[pho_n]
   Float_t         pho_e1x5[100];   //[pho_n]
   Float_t         pho_e3x3[100];   //[pho_n]
   Float_t         pho_e5x5[100];   //[pho_n]
   Float_t         pho_emaxxtal[28];   //[pho_n]
   Float_t         pho_r9[28];   //[pho_n]
   Float_t         pho_e2nd[28];   //[pho_n]
   Float_t         pho_e2x5max[28];   //[pho_n]
   Float_t         pho_e2x5right[28];   //[pho_n]
   Float_t         pho_e2x5left[28];   //[pho_n]
   Float_t         pho_e2x5top[28];   //[pho_n]
   Float_t         pho_e2x5bottom[28];   //[pho_n]
   Float_t         pho_eright[28];   //[pho_n]
   Float_t         pho_eleft[28];   //[pho_n]
   Float_t         pho_etop[28];   //[pho_n]
   Float_t         pho_ebottom[28];   //[pho_n]
   Float_t         pho_etawidth[28];   //[pho_n]
   Float_t         pho_e2x2[100];   //[pho_n]
   Float_t         pho_ecalsumetconedr04[28];   //[pho_n]
   Float_t         pho_ecalsumetconedr03[28];   //[pho_n]
   TClonesArray    *pho_p4;
   TClonesArray    *sc_p4;
   Int_t           pho_scind[28];   //[pho_n]
   Float_t         pho_eseffsixix[28];   //[pho_n]
   Float_t         pho_eseffsiyiy[28];   //[pho_n]
   Float_t         pho_hoe_bc[28];   //[pho_n]
   Int_t           vtx_std_n;
   Float_t         rho_algo1;
   Float_t         pho_e5x5_cleaned[28];   //[pho_n]
   Float_t         pho_e2x2_cleaned[100];   //[pho_n]
   Int_t           dipho_n;
   Int_t           dipho_vtxind[49];   //[dipho_n]
   Bool_t          pho_genmatched[100];   //[pho_n]
   Float_t         pho_genenergy[100];   //[pho_n]
   Int_t           pho_biphi[100];
   Int_t           pho_bieta[100];
   Float_t           pho_betacry[100];
   Float_t           pho_bphicry[100];

   //Double_t be2nd;
   //Double_t betop;
   //Double_t bebottom;
   //Double_t beleft;
   //Double_t beright;
   //
   //Double_t be2x5max;
   //Double_t be2x5top;
   //Double_t be2x5bottom;
   //Double_t be2x5left;
   //Double_t be2x5right;
   //Double_t pre;


   // List of branches
   TBranch *b_sc_p4;
   TBranch        *b_sc_xyz;   //!
   TBranch        *b_sc_n;   //!
   TBranch        *b_sc_sphi;   //!
   TBranch        *b_sc_seta;   //!
   TBranch        *b_sc_raw;   //!
   TBranch        *b_sc_pre;   //!
   TBranch        *b_sc_bcseedind;   //!
   TBranch        *b_sc_nbc;   //!
   TBranch        *b_bc_n;   //!
   TBranch        *b_bc_p4;   //!
   TBranch        *b_bc_s25;   //!
   TBranch        *b_pho_n;   //!
   TBranch        *b_pho_sieie;   //!
   TBranch        *b_pho_sieip;   //!
   TBranch        *b_pho_sipip;   //!
   TBranch        *b_pho_e1x5;   //!
   TBranch        *b_pho_e3x3;   //!
   TBranch        *b_pho_e5x5;   //!
   TBranch        *b_pho_emaxxtal;   //!
   TBranch        *b_pho_r9;   //!
   TBranch        *b_pho_e2nd;   //!
   TBranch        *b_pho_e2x5max;   //!
   TBranch        *b_pho_e2x5right;   //!
   TBranch        *b_pho_e2x5left;   //!
   TBranch        *b_pho_e2x5top;   //!
   TBranch        *b_pho_e2x5bottom;   //!
   TBranch        *b_pho_eright;   //!
   TBranch        *b_pho_eleft;   //!
   TBranch        *b_pho_etop;   //!
   TBranch        *b_pho_ebottom;   //!
   TBranch        *b_pho_etawidth;   //!
   TBranch        *b_pho_e2x2;   //!
   TBranch        *b_pho_ecalsumetconedr04;   //!
   TBranch        *b_pho_ecalsumetconedr03;   //!
   TBranch        *b_pho_p4;   //!
   TBranch        *b_pho_scind;   //!
   TBranch        *b_pho_eseffsixix;   //!
   TBranch        *b_pho_eseffsiyiy;   //!
   TBranch        *b_pho_hoe_bc;   //!
   TBranch        *b_vtx_std_n;   //!
   TBranch        *b_rho_algo1;   //!
   TBranch        *b_pho_e5x5_cleaned;   //!
   TBranch        *b_pho_e2x2_cleaned;   //!
   TBranch        *b_dipho_n;   //!
   TBranch        *b_dipho_vtxind;   //!
   TBranch        *b_pho_genmatched;   //!
   TBranch        *b_pho_genenergy;   //!
   TBranch        *b_event;
   TBranch        *b_pho_biphi;
   TBranch        *b_pho_bieta;
   TBranch        *b_pho_betacry;
   TBranch        *b_pho_bphicry;


 RegressionTreeMaker2(TTree * /*tree*/ =0) : fChain(0) { outTree = 0;}
   virtual ~RegressionTreeMaker2() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

   ClassDef(RegressionTreeMaker2,0);
};

#endif

#ifdef RegressionTreeMaker2_cxx
void RegressionTreeMaker2::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
  sc_xyz = new TClonesArray("TVector3");
  pho_p4 = new TClonesArray("TLorentzVector");
  bc_p4 = new TClonesArray("TLorentzVector");
  sc_p4 = new TClonesArray("TLorentzVector");

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("sc_xyz", &sc_xyz, &b_sc_xyz);
   fChain->SetBranchAddress("sc_n", &sc_n, &b_sc_n);
   fChain->SetBranchAddress("sc_sphi", sc_sphi, &b_sc_sphi);
   fChain->SetBranchAddress("sc_seta", sc_seta, &b_sc_seta);
   fChain->SetBranchAddress("sc_raw", sc_raw, &b_sc_raw);
   //fChain->SetBranchAddress("sc_pre", sc_pre, &b_sc_pre);
   fChain->SetBranchAddress("sc_bcseedind", sc_bcseedind, &b_sc_bcseedind);
   fChain->SetBranchAddress("sc_nbc", sc_nbc, &b_sc_nbc);
   fChain->SetBranchAddress("bc_n", &bc_n, &b_bc_n);
   fChain->SetBranchAddress("bc_p4", &bc_p4, &b_bc_p4);
   fChain->SetBranchAddress("bc_s25", bc_s25, &b_bc_s25);
   fChain->SetBranchAddress("pho_n", &pho_n, &b_pho_n);
   fChain->SetBranchAddress("pho_sieie", pho_sieie, &b_pho_sieie);
   fChain->SetBranchAddress("pho_sieip", pho_sieip, &b_pho_sieip);
   fChain->SetBranchAddress("pho_sipip", pho_sipip, &b_pho_sipip);
   fChain->SetBranchAddress("pho_e1x5", pho_e1x5, &b_pho_e1x5);
   fChain->SetBranchAddress("pho_e3x3", pho_e3x3, &b_pho_e3x3);
   fChain->SetBranchAddress("pho_e5x5", pho_e5x5, &b_pho_e5x5);
   fChain->SetBranchAddress("pho_emaxxtal", pho_emaxxtal, &b_pho_emaxxtal);
   fChain->SetBranchAddress("pho_r9", pho_r9, &b_pho_r9);
   fChain->SetBranchAddress("pho_e2nd", pho_e2nd, &b_pho_e2nd);
   fChain->SetBranchAddress("pho_e2x5max", pho_e2x5max, &b_pho_e2x5max);
   fChain->SetBranchAddress("pho_e2x5right", pho_e2x5right, &b_pho_e2x5right);
   fChain->SetBranchAddress("pho_e2x5left", pho_e2x5left, &b_pho_e2x5left);
   fChain->SetBranchAddress("pho_e2x5top", pho_e2x5top, &b_pho_e2x5top);
   fChain->SetBranchAddress("pho_e2x5bottom", pho_e2x5bottom, &b_pho_e2x5bottom);
   fChain->SetBranchAddress("pho_eright", pho_eright, &b_pho_eright);
   fChain->SetBranchAddress("pho_eleft", pho_eleft, &b_pho_eleft);
   fChain->SetBranchAddress("pho_etop", pho_etop, &b_pho_etop);
   fChain->SetBranchAddress("pho_ebottom", pho_ebottom, &b_pho_ebottom);
   fChain->SetBranchAddress("pho_etawidth", pho_etawidth, &b_pho_etawidth);
   fChain->SetBranchAddress("pho_e2x2", pho_e2x2, &b_pho_e2x2);
   //fChain->SetBranchAddress("pho_ecalsumetconedr04", pho_ecalsumetconedr04, &b_pho_ecalsumetconedr04);
   //fChain->SetBranchAddress("pho_ecalsumetconedr03", pho_ecalsumetconedr03, &b_pho_ecalsumetconedr03);
   fChain->SetBranchAddress("pho_p4", &pho_p4, &b_pho_p4);
   fChain->SetBranchAddress("sc_p4", &sc_p4, &b_sc_p4);
   fChain->SetBranchAddress("pho_scind", pho_scind, &b_pho_scind);
   //fChain->SetBranchAddress("pho_eseffsixix", pho_eseffsixix, &b_pho_eseffsixix);
   //fChain->SetBranchAddress("pho_eseffsiyiy", pho_eseffsiyiy, &b_pho_eseffsiyiy);
   fChain->SetBranchAddress("pho_hoe", pho_hoe_bc, &b_pho_hoe_bc);
   fChain->SetBranchAddress("vtx_std_n", &vtx_std_n, &b_vtx_std_n);
   fChain->SetBranchAddress("rho_algo1", &rho_algo1, &b_rho_algo1);
   fChain->SetBranchAddress("pho_bieta", pho_bieta, &b_pho_bieta);
   fChain->SetBranchAddress("pho_biphi", pho_biphi, &b_pho_biphi);
   fChain->SetBranchAddress("pho_betacry", pho_betacry, &b_pho_betacry);
   fChain->SetBranchAddress("pho_phicry", pho_bphicry, &b_pho_bphicry);
   fChain->SetBranchAddress("dipho_n", &dipho_n, &b_dipho_n);
   fChain->SetBranchAddress("dipho_vtxind", dipho_vtxind, &b_dipho_vtxind);
   fChain->SetBranchAddress("pho_genmatched", pho_genmatched, &b_pho_genmatched);
   fChain->SetBranchAddress("pho_genenergy", pho_genenergy, &b_pho_genenergy);
}

Bool_t RegressionTreeMaker2::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

#endif // #ifdef RegressionTreeMaker2_cxx
