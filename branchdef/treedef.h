Int_t pho_ncrys[MAX_PHOTONS];
Int_t pfcand_n;
Int_t pfcand_pdgid[MAX_PFCANDS];
TClonesArray* pfcand_p4;
TClonesArray* pfcand_posvtx;
Int_t lumis;
Int_t bx;
Int_t event;
Int_t run;
Int_t process_id;
Float_t weight;
Float_t pthat;
TClonesArray *ct_p4;
Int_t ct_n;
Float_t ct_emEnergy[MAX_CALOTOWERS];
Float_t ct_hadEnergy[MAX_CALOTOWERS];
Float_t ct_outerEnergy[MAX_CALOTOWERS];
Int_t ct_emL1[MAX_CALOTOWERS];
Int_t ct_hadL1[MAX_CALOTOWERS];
Int_t ct_size[MAX_CALOTOWERS];
TClonesArray *sc_p4;
TClonesArray *sc_islbar_p4;
TClonesArray *sc_xyz;
TClonesArray *sc_islbar_xyz;
TClonesArray *bc_p4;
TClonesArray *bc_xyz;
Int_t sc_islbar_n;
Float_t sc_islbar_raw[MAX_SUPERCLUSTERS];
Float_t sc_islbar_seedenergy[MAX_SUPERCLUSTERS];
Int_t sc_islbar_nbc[MAX_SUPERCLUSTERS];
Int_t sc_islbar_bcseedind[MAX_SUPERCLUSTERS];
Int_t sc_islbar_bcind[MAX_SUPERCLUSTERS][MAX_SUPERCLUSTER_BASICCLUSTERS];
Int_t sc_n;
Int_t sc_hybrid_n;
Int_t sc_islend_n;
Float_t sc_pre[MAX_SUPERCLUSTERS];
Float_t sc_raw[MAX_SUPERCLUSTERS];
Int_t sc_nbc[MAX_SUPERCLUSTERS];
Int_t sc_bcseedind[MAX_SUPERCLUSTERS];

Float_t sc_bcseed_sMax[MAX_SUPERCLUSTERS]; 
Float_t sc_bcseed_s2nd[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_top[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_bottom[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_left[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_right[MAX_SUPERCLUSTERS];

Float_t sc_bcseed_2x5max[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_2x5top[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_2x5bottom[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_2x5left[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_2x5right[MAX_SUPERCLUSTERS];

Int_t sc_bcseed_ieta[MAX_SUPERCLUSTERS];   
Int_t sc_bcseed_iphi[MAX_SUPERCLUSTERS];
Float_t sc_bcseed_etacry[MAX_SUPERCLUSTERS];  
Float_t sc_bcseed_phicry[MAX_SUPERCLUSTERS]; 


Int_t sc_bcind[MAX_SUPERCLUSTERS][MAX_SUPERCLUSTER_BASICCLUSTERS];
Int_t sc_barrel[MAX_SUPERCLUSTERS];
Float_t sc_2xN[MAX_SUPERCLUSTERS];
Float_t sc_5xN[MAX_SUPERCLUSTERS];
Float_t sc_sieie[MAX_SUPERCLUSTERS];
Float_t sc_seta[MAX_SUPERCLUSTERS];
Float_t sc_sphi[MAX_SUPERCLUSTERS];
Float_t sc_see[MAX_SUPERCLUSTERS];
Int_t bc_n;
Int_t bc_hybrid_n;
Int_t bc_islbar_n;
Int_t bc_islend_n;
Int_t bc_nhits[MAX_BASICCLUSTERS];
Int_t bc_type[MAX_BASICCLUSTERS];
Float_t bc_rook[MAX_BASICCLUSTERS];
Float_t bc_s1[MAX_BASICCLUSTERS];
Float_t bc_s4[MAX_BASICCLUSTERS];
Float_t bc_s9[MAX_BASICCLUSTERS];
Float_t bc_s25[MAX_BASICCLUSTERS];
Float_t bc_spp[MAX_BASICCLUSTERS];
Float_t bc_see[MAX_BASICCLUSTERS];
Float_t bc_sep[MAX_BASICCLUSTERS];
Float_t bc_chx[MAX_BASICCLUSTERS];
Float_t bc_s1x5_0[MAX_BASICCLUSTERS];
Float_t bc_s1x5_1[MAX_BASICCLUSTERS];
Float_t bc_s1x5_2[MAX_BASICCLUSTERS];
Float_t bc_s1x3_0[MAX_BASICCLUSTERS];
Float_t bc_s1x3_1[MAX_BASICCLUSTERS];
Float_t bc_s1x3_2[MAX_BASICCLUSTERS];
Float_t bc_s5x1_0[MAX_BASICCLUSTERS];
Float_t bc_s5x1_1[MAX_BASICCLUSTERS];
Float_t bc_s5x1_2[MAX_BASICCLUSTERS];
Float_t bc_s3x1_0[MAX_BASICCLUSTERS];
Float_t bc_s3x1_1[MAX_BASICCLUSTERS];
Float_t bc_s3x1_2[MAX_BASICCLUSTERS];
Float_t bc_sieie[MAX_BASICCLUSTERS];
Float_t bc_sipip[MAX_BASICCLUSTERS];
Float_t bc_sieip[MAX_BASICCLUSTERS];
Float_t bc_2x5_max[MAX_BASICCLUSTERS];
Float_t bc_5x1_sam[MAX_BASICCLUSTERS];
Int_t bc_seed[MAX_BASICCLUSTERS];
TClonesArray *ecalhit_p4;
Int_t ecalhit_n;
Float_t ecalhit_time[MAX_ECALRECHITS];
UInt_t ecalhit_detid[MAX_ECALRECHITS];
Short_t ecalhit_type[MAX_ECALRECHITS];
Short_t ecalhit_flag[MAX_ECALRECHITS];
Int_t el_std_n;
Float_t el_std_enearbcopin[MAX_ELECTRONS];
Float_t el_std_eseedopout[MAX_ELECTRONS];
Float_t el_std_eopin[MAX_ELECTRONS];
Float_t el_std_pout[MAX_ELECTRONS];
Float_t el_std_pin[MAX_ELECTRONS];
Float_t el_std_fbrem[MAX_ELECTRONS];
Int_t el_std_nbrem[MAX_ELECTRONS];
Int_t el_std_1pxb[MAX_ELECTRONS];
Int_t el_std_1pxf[MAX_ELECTRONS];
Float_t el_std_hoe[MAX_ELECTRONS];
Float_t el_std_hoed1[MAX_ELECTRONS];
Float_t el_std_hoed2[MAX_ELECTRONS];
Float_t el_std_detain[MAX_ELECTRONS];
Float_t el_std_dphiin[MAX_ELECTRONS];
Float_t el_std_detaout[MAX_ELECTRONS];
Float_t el_std_dphiout[MAX_ELECTRONS];
Float_t el_std_z0[MAX_ELECTRONS];
Float_t el_std_d0[MAX_ELECTRONS];
Float_t el_std_D0Vtx[MAX_ELECTRONS][100];
Float_t el_std_DZVtx[MAX_ELECTRONS][100];
Float_t el_std_z0err[MAX_ELECTRONS];
Float_t el_std_d0err[MAX_ELECTRONS];
Float_t el_std_chi2[MAX_ELECTRONS];
Float_t el_std_dof[MAX_ELECTRONS];
Float_t el_std_e1x5[MAX_ELECTRONS];
Float_t el_std_e5x5[MAX_ELECTRONS];
Float_t el_std_spp[MAX_ELECTRONS];
Float_t el_std_see[MAX_ELECTRONS];
Float_t el_std_sieie[MAX_ELECTRONS];
Float_t el_std_sieiesc[MAX_ELECTRONS];
Float_t el_std_sieie_nolog[MAX_ELECTRONS];
Float_t el_std_sieiesc_nolog[MAX_ELECTRONS];
Float_t el_std_e2x5[MAX_ELECTRONS];
Float_t el_std_esc[MAX_ELECTRONS];
Float_t el_std_eseed[MAX_ELECTRONS];
Float_t el_std_eseedopin[MAX_ELECTRONS];
Float_t el_std_qoverperr[MAX_ELECTRONS];
Float_t el_std_pterr[MAX_ELECTRONS];
Float_t el_std_etaerr[MAX_ELECTRONS];
Float_t el_std_phierr[MAX_ELECTRONS];
Int_t el_std_class[MAX_ELECTRONS];
Int_t el_std_charge[MAX_ELECTRONS];
Int_t el_std_ch_gsf[MAX_ELECTRONS];
Int_t el_std_ch_scpix[MAX_ELECTRONS];
Int_t el_std_losthits[MAX_ELECTRONS];
Int_t el_std_validhits[MAX_ELECTRONS];
Int_t el_std_hp_expin[MAX_ELECTRONS];
Int_t el_std_hp_expin2[MAX_ELECTRONS];
Int_t el_std_hp_expout[MAX_ELECTRONS];
Int_t el_std_scind[MAX_ELECTRONS];
Int_t el_std_crack[MAX_ELECTRONS];
Int_t el_std_tkind[MAX_ELECTRONS];
Int_t el_std_nambtk[MAX_ELECTRONS];
Int_t el_std_roloose[MAX_ELECTRONS];
Int_t el_std_rotight[MAX_ELECTRONS];
Int_t el_std_rohighe[MAX_ELECTRONS];
Int_t el_std_loose[MAX_ELECTRONS]; 
Int_t el_std_tight[MAX_ELECTRONS];
Float_t el_std_tkiso03[MAX_ELECTRONS];
Float_t el_std_ecaliso03[MAX_ELECTRONS];
Float_t el_std_hcaliso03[MAX_ELECTRONS];
Float_t el_std_tkiso04[MAX_ELECTRONS];
Float_t el_std_ecaliso04[MAX_ELECTRONS];
Float_t el_std_hcaliso04[MAX_ELECTRONS];
Float_t el_std_mva[MAX_ELECTRONS];
Float_t el_std_mva_trig[MAX_ELECTRONS];
Float_t el_std_mva_nontrig[MAX_ELECTRONS];
Bool_t el_std_ecaldrv[MAX_ELECTRONS];
Bool_t el_std_tkdrv[MAX_ELECTRONS];
Float_t el_std_ip_ctf[MAX_ELECTRONS];
Float_t el_std_ip_gsf[MAX_ELECTRONS];
Float_t el_std_dist[MAX_ELECTRONS];
Float_t el_std_dcot[MAX_ELECTRONS];
std::vector<std::vector<int> >* el_std_catbased;
TClonesArray *el_std_sc;
TClonesArray *el_std_p4;
TClonesArray *el_std_momvtx;
TClonesArray *el_std_momvtxconst;
TClonesArray *el_std_momcalo;
TClonesArray *el_std_momout;
TClonesArray *el_std_posvtx;
TClonesArray *el_std_poscalo;
Int_t gp_n;
Short_t gp_status[MAX_GENERATOR];
Short_t gp_pdgid[MAX_GENERATOR];
Short_t gp_mother[MAX_GENERATOR];
TClonesArray *gp_p4;
TClonesArray *gp_vtx;
Int_t genjet_algo1_n;
Float_t genjet_algo1_em[MAX_GENJETS]; 
Float_t genjet_algo1_had[MAX_GENJETS]; 
Float_t genjet_algo1_inv[MAX_GENJETS]; 
Float_t genjet_algo1_aux[MAX_GENJETS];
TClonesArray *genjet_algo1_p4;
Int_t genjet_algo2_n;
Float_t genjet_algo2_em[MAX_GENJETS]; 
Float_t genjet_algo2_had[MAX_GENJETS]; 
Float_t genjet_algo2_inv[MAX_GENJETS]; 
Float_t genjet_algo2_aux[MAX_GENJETS];
TClonesArray *genjet_algo2_p4;
Int_t genjet_algo3_n;
Float_t genjet_algo3_em[MAX_GENJETS]; 
Float_t genjet_algo3_had[MAX_GENJETS]; 
Float_t genjet_algo3_inv[MAX_GENJETS]; 
Float_t genjet_algo3_aux[MAX_GENJETS];
TClonesArray *genjet_algo3_p4;
TClonesArray *hc_p4;
Int_t hc_type[MAX_HCALHITS];
Int_t hc_n;
std::vector<unsigned short>* hlt_bit;
std::vector<unsigned short>* hlt1_bit;
std::vector<unsigned short>* hlt2_bit;
Int_t hlt_n;
std::vector<std::vector<unsigned short> >* hlt_candpath;
std::vector<std::string> *hlt_path_names_HLT;
std::vector<std::string> *hlt_path_names_HLT1;
std::vector<std::string> *hlt_path_names_HLT2;
TClonesArray* hlt_p4;
Float_t rho_algo1;
Float_t rho_algo2;
Float_t rho_algo3;
Float_t ht_nomet25;
Float_t ht_nomet35;
Float_t ht_nomet50;
Float_t ht_trk;
Float_t ht_25;
Float_t ht_35;
Float_t ht_50;
TVector3 *ht_trkvec;
Int_t ht_2lpt_n;
Int_t ht_2lpt_inds[MAX_HT2][2];
Float_t ht_2lpt25[MAX_HT2];
Float_t ht_2lpt35[MAX_HT2];
Float_t ht_2lpt50[MAX_HT2];
Int_t ht_4lpt_n;
Int_t ht_4lpt_inds[MAX_HT4][4];
Float_t ht_4lpt25[MAX_HT4];
Float_t ht_4lpt35[MAX_HT4];
Float_t ht_4lpt50[MAX_HT4];
Int_t jet_algo1_n;
Float_t jet_algo1_emfrac[MAX_JETS];
Float_t jet_algo1_hadfrac[MAX_JETS];
Int_t jet_algo1_ntk[MAX_JETS];
Int_t jet_algo1_ncalotw[MAX_JETS];
std::vector<std::vector<unsigned short> >* jet_algo1_calotwind;
std::vector<std::vector<unsigned short> >* jet_algo1_tkind;
TClonesArray *jet_algo1_p4;
Int_t jet_algo2_n;
Float_t jet_algo2_emfrac[MAX_JETS];
Float_t jet_algo2_hadfrac[MAX_JETS];
Int_t jet_algo2_ntk[MAX_JETS];
Int_t jet_algo2_ncalotw[MAX_JETS];
std::vector<std::vector<unsigned short> >* jet_algo2_calotwind;
std::vector<std::vector<unsigned short> >* jet_algo2_tkind;
TClonesArray *jet_algo2_p4;
Int_t jet_algo3_n;
Float_t jet_algo3_emfrac[MAX_JETS];
Float_t jet_algo3_hadfrac[MAX_JETS];
Int_t jet_algo3_ntk[MAX_JETS];
Int_t jet_algo3_ncalotw[MAX_JETS];
std::vector<std::vector<unsigned short> >* jet_algo3_calotwind;
std::vector<std::vector<unsigned short> >* jet_algo3_tkind;
TClonesArray *jet_algo3_p4;
Int_t jet_algoPF1_n;
Int_t jet_algoPF1_nvtx;
Float_t jet_algoPF1_emfrac[MAX_JETS];
Float_t jet_algoPF1_hadfrac[MAX_JETS];
Float_t jet_algoPF1_erescale[MAX_JETS];
Int_t jet_algoPF1_ntk[MAX_JETS];
Int_t jet_algoPF1_ncalotw[MAX_JETS];
std::vector<std::vector<unsigned short> >* jet_algoPF1_calotwind;
std::vector<std::vector<unsigned short> >* jet_algoPF1_tkind;
TClonesArray *jet_algoPF1_p4;
Float_t jet_algoPF1_beta[MAX_JETS];
Float_t jet_algoPF1_betaStar[MAX_JETS];
Float_t jet_algoPF1_betaStarClassic[MAX_JETS];
Float_t jet_algoPF1_dR2Mean[MAX_JETS];
Float_t jet_algoPF1_dRMean[MAX_JETS];
Float_t jet_algoPF1_dZ[MAX_JETS];
Float_t jet_algoPF1_frac01[MAX_JETS];
Float_t jet_algoPF1_frac02[MAX_JETS];
Float_t jet_algoPF1_frac03[MAX_JETS];
Float_t jet_algoPF1_frac04[MAX_JETS];
Float_t jet_algoPF1_frac05[MAX_JETS];
Float_t jet_algoPF1_full_mva[MAX_JETS];
Float_t jet_algoPF1_simple_mva[MAX_JETS];
Float_t jet_algoPF1_nCharged[MAX_JETS];
Float_t jet_algoPF1_nNeutrals[MAX_JETS];
Int_t jet_algoPF1_full_wp_level[MAX_JETS];
Int_t jet_algoPF1_simple_wp_level[MAX_JETS];
Int_t jet_algoPF2_n;
Float_t jet_algoPF2_emfrac[MAX_JETS];
Float_t jet_algoPF2_hadfrac[MAX_JETS];
Float_t jet_algoPF2_erescale[MAX_JETS];
Int_t jet_algoPF2_ntk[MAX_JETS];
Int_t jet_algoPF2_ncalotw[MAX_JETS];
std::vector<std::vector<unsigned short> >* jet_algoPF2_calotwind;
std::vector<std::vector<unsigned short> >* jet_algoPF2_tkind;
TClonesArray *jet_algoPF2_p4;
Float_t jet_algoPF2_beta[MAX_JETS];
Float_t jet_algoPF2_betaStar[MAX_JETS];
Float_t jet_algoPF2_betaStarClassic[MAX_JETS];
Float_t jet_algoPF2_dR2Mean[MAX_JETS];
Float_t jet_algoPF2_dRMean[MAX_JETS];
Float_t jet_algoPF2_dZ[MAX_JETS];
Float_t jet_algoPF2_frac01[MAX_JETS];
Float_t jet_algoPF2_frac02[MAX_JETS];
Float_t jet_algoPF2_frac03[MAX_JETS];
Float_t jet_algoPF2_frac04[MAX_JETS];
Float_t jet_algoPF2_frac05[MAX_JETS];
Float_t jet_algoPF2_full_mva[MAX_JETS];
Float_t jet_algoPF2_simple_mva[MAX_JETS];
Float_t jet_algoPF2_nCharged[MAX_JETS];
Float_t jet_algoPF2_nNeutrals[MAX_JETS];
Int_t jet_algoPF2_full_wp_level[MAX_JETS];
Int_t jet_algoPF2_simple_wp_level[MAX_JETS];
Int_t jet_algoPF3_n;
Int_t jet_algoPF3_nvtx;
Float_t jet_algoPF3_emfrac[MAX_JETS];
Float_t jet_algoPF3_hadfrac[MAX_JETS];
Float_t jet_algoPF3_erescale[MAX_JETS];
Int_t jet_algoPF3_ntk[MAX_JETS];
Int_t jet_algoPF3_ncalotw[MAX_JETS];
std::vector<std::vector<unsigned short> >* jet_algoPF3_calotwind;
std::vector<std::vector<unsigned short> >* jet_algoPF3_tkind;
TClonesArray *jet_algoPF3_p4;
Float_t jet_algoPF3_beta[MAX_JETS];
Float_t jet_algoPF3_betaStar[MAX_JETS];
Float_t jet_algoPF3_betaStarClassic[MAX_JETS];
Float_t jet_algoPF3_dR2Mean[MAX_JETS];
Float_t jet_algoPF3_dRMean[MAX_JETS];
Float_t jet_algoPF3_dZ[MAX_JETS];
Float_t jet_algoPF3_frac01[MAX_JETS];
Float_t jet_algoPF3_frac02[MAX_JETS];
Float_t jet_algoPF3_frac03[MAX_JETS];
Float_t jet_algoPF3_frac04[MAX_JETS];
Float_t jet_algoPF3_frac05[MAX_JETS];
Float_t jet_algoPF3_full_mva[MAX_JETS];
Float_t jet_algoPF3_simple_mva[MAX_JETS];
Float_t jet_algoPF3_nCharged[MAX_JETS];
Float_t jet_algoPF3_nNeutrals[MAX_JETS];
Int_t jet_algoPF3_full_wp_level[MAX_JETS];
Int_t jet_algoPF3_simple_wp_level[MAX_JETS];

Float_t jet_algoPF1_csvBtag[MAX_JETS];
Float_t jet_algoPF1_csvMvaBtag[MAX_JETS];
Float_t jet_algoPF1_jetProbBtag[MAX_JETS];
Float_t jet_algoPF1_tcheBtag[MAX_JETS];

Float_t jet_algoPF2_csvBtag[MAX_JETS];
Float_t jet_algoPF2_csvMvaBtag[MAX_JETS];
Float_t jet_algoPF2_jetProbBtag[MAX_JETS];
Float_t jet_algoPF2_tcheBtag[MAX_JETS];

Float_t jet_algoPF3_csvBtag[MAX_JETS];
Float_t jet_algoPF3_csvMvaBtag[MAX_JETS];
Float_t jet_algoPF3_jetProbBtag[MAX_JETS];
Float_t jet_algoPF3_tcheBtag[MAX_JETS];

Int_t l1emiso_n;
Float_t l1emiso_et[MAX_L1]; 
Float_t l1emiso_eta[MAX_L1]; 
Float_t l1emiso_phi[MAX_L1];
Int_t l1emnoniso_n;
Float_t l1emnoniso_et[MAX_L1];
Float_t l1emnoniso_eta[MAX_L1];
Float_t l1emnoniso_phi[MAX_L1];
Int_t l1cenjet_n;
Float_t l1cenjet_et[MAX_L1];
Float_t l1cenjet_eta[MAX_L1];
Float_t l1cenjet_phi[MAX_L1];
Int_t l1forjet_n;
Float_t l1forjet_et[MAX_L1];
Float_t l1forjet_eta[MAX_L1];
Float_t l1forjet_phi[MAX_L1];
Int_t l1taujet_n;
Float_t l1taujet_et[MAX_L1];
Float_t l1taujet_eta[MAX_L1];
Float_t l1taujet_phi[MAX_L1];
Float_t l1met_et;
Float_t l1met_phi;
Int_t l1mu_n;
Float_t l1mu_et[MAX_L1];
Float_t l1mu_eta[MAX_L1];
Float_t l1mu_phi[MAX_L1];
std::vector<int>* l1bits_phy;
std::vector<int>* l1bits_tec;
std::map<std::string, int>* l1_labels;
Int_t lpt_n;
Int_t lpt_mu_n;
Int_t lpt_el_n;
Int_t lpt_emu_n;
Int_t lpt_pho_n;
Int_t lpt_pdgid[MAX_LEPTONS];
Int_t lpt_ind[MAX_LEPTONS];
Int_t lpt_duplicate[MAX_LEPTONS];
Int_t lpt_indgen[MAX_LEPTONS];
Float_t lpt_drmatch[MAX_LEPTONS];
TClonesArray *lpt_p4;
Float_t met_met;
Float_t met_phi;
Float_t met_met_nocalo;
Float_t met_phi_nocalo;
Float_t met_met_crossed;
Float_t met_phi_crossed;
Float_t met_met_s9;
Float_t met_phi_s9;
Float_t met_met_mip;
Float_t met_phi_mip;
Float_t met_met_jet;
Float_t met_phi_jet;
Float_t met_tcmet;
Float_t met_phi_tcmet;
Float_t met_pfmet;
Float_t met_phi_pfmet;
Float_t met_sumet_pfmet;
Float_t met_mEtSig_pfmet;
Float_t met_significance_pfmet;
Float_t met_pfmetType1;
Float_t met_phi_pfmetType1;
Float_t met_sumet_pfmetType1;
Float_t met_mEtSig_pfmetType1;
Float_t met_significance_pfmetType1;
Int_t mu_glo_n;
Float_t mu_glo_em[MAX_MUONS];
Float_t mu_glo_had[MAX_MUONS];
Float_t mu_glo_ho[MAX_MUONS];
Float_t mu_glo_emS9[MAX_MUONS];
Float_t mu_glo_hadS9[MAX_MUONS];
Float_t mu_glo_hoS9[MAX_MUONS];
Float_t mu_glo_z0[MAX_MUONS];
Float_t mu_glo_d0[MAX_MUONS];
Float_t mu_glo_D0Vtx[MAX_MUONS][100];
Float_t mu_glo_DZVtx[MAX_MUONS][100];
Float_t mu_glo_z0err[MAX_MUONS];
Float_t mu_glo_d0err[MAX_MUONS];
Float_t mu_glo_chi2[MAX_MUONS];
Float_t mu_glo_dof[MAX_MUONS];
Int_t mu_glo_charge[MAX_MUONS];
Int_t mu_glo_losthits[MAX_MUONS];
Int_t mu_glo_validhits[MAX_MUONS];
Int_t mu_glo_innerhits[MAX_MUONS];
Int_t mu_glo_tkind[MAX_MUONS];
Int_t mu_glo_nmatches[MAX_MUONS];
Int_t mu_glo_staind[MAX_MUONS];
Int_t mu_glo_type[MAX_MUONS];
Float_t mu_glo_iso[MAX_MUONS];
Int_t mu_glo_pixelhits[MAX_MUONS];
Int_t mu_glo_validChmbhits[MAX_MUONS];
Float_t mu_glo_tkpterr[MAX_MUONS];
Float_t mu_glo_ecaliso03[MAX_MUONS];
Float_t mu_glo_hcaliso03[MAX_MUONS];
Float_t mu_glo_tkiso03[MAX_MUONS];
Float_t mu_glo_dz[MAX_MUONS];
//MU ID 2012
Int_t mu_tkLayers[MAX_MUONS];
Float_t mu_glo_chhadiso04[MAX_MUONS];
Float_t mu_glo_nehadiso04[MAX_MUONS];
Float_t mu_glo_photiso04[MAX_MUONS];
Float_t mu_dbCorr[MAX_MUONS];
//
TClonesArray *mu_glo_p4;
TClonesArray *mu_glo_momvtx;
TClonesArray *mu_glo_posvtx;
TClonesArray *mu_glo_poshcal;
TClonesArray *mu_glo_posecal;
Int_t pho_n;
Float_t pho_feta[MAX_PHOTONS][5];
Float_t pho_crackcorr[MAX_PHOTONS];
Float_t pho_localcorr[MAX_PHOTONS];
Int_t pho_isEB[MAX_PHOTONS];
Int_t pho_isEE[MAX_PHOTONS];
Int_t pho_isEBGap[MAX_PHOTONS];
Int_t pho_isEEGap[MAX_PHOTONS];
Int_t pho_isEBEEGap[MAX_PHOTONS];
Float_t pho_see[MAX_PHOTONS];
Float_t pho_sieie[MAX_PHOTONS];
Float_t pho_sipip[MAX_PHOTONS];
Float_t pho_sieip[MAX_PHOTONS];
Float_t pho_e1x5[MAX_PHOTONS];
Float_t pho_e2x5[MAX_PHOTONS];
Float_t pho_e3x3[MAX_PHOTONS];
Float_t pho_e5x5[MAX_PHOTONS];
Float_t pho_emaxxtal[MAX_PHOTONS];
Float_t pho_hoe[MAX_PHOTONS];
Float_t pho_h1oe[MAX_PHOTONS];
Float_t pho_h2oe[MAX_PHOTONS];
Float_t pho_r1x5[MAX_PHOTONS];
Float_t pho_r2x5[MAX_PHOTONS];
Float_t pho_r9[MAX_PHOTONS];
Float_t pho_zernike20[MAX_PHOTONS];
Float_t pho_zernike42[MAX_PHOTONS];
Float_t pho_e2nd[MAX_PHOTONS];
Float_t pho_e2x5right[MAX_PHOTONS];
Float_t pho_e2x5left[MAX_PHOTONS];
Float_t pho_e2x5top[MAX_PHOTONS];
Float_t pho_e2x5max[MAX_PHOTONS];
Int_t pho_bieta[MAX_PHOTONS];
Int_t pho_biphi[MAX_PHOTONS];
Float_t pho_betacry[MAX_PHOTONS];
Float_t pho_phicry[MAX_PHOTONS];
Float_t pho_bthetatilt[MAX_PHOTONS];
Float_t pho_bphitilt[MAX_PHOTONS];
Float_t pho_e2x5bottom[MAX_PHOTONS];
Float_t pho_eright[MAX_PHOTONS];
Float_t pho_eleft[MAX_PHOTONS];
Float_t pho_etop[MAX_PHOTONS];
Float_t pho_ebottom[MAX_PHOTONS];
Float_t pho_e2overe9[MAX_PHOTONS];
Float_t pho_seed_time[MAX_PHOTONS];
Float_t pho_seed_outoftimechi2[MAX_PHOTONS];
Float_t pho_seed_chi2[MAX_PHOTONS];
Float_t pho_seed_recoflag[MAX_PHOTONS];
Float_t pho_seed_severity[MAX_PHOTONS];
Float_t pho_ecalsumetconedr04[MAX_PHOTONS];
Float_t pho_hcalsumetconedr04[MAX_PHOTONS];
Float_t pho_hcal1sumetconedr04[MAX_PHOTONS];
Float_t pho_hcal2sumetconedr04[MAX_PHOTONS];
Float_t pho_trksumptsolidconedr04[MAX_PHOTONS];
Float_t pho_trksumpthollowconedr04[MAX_PHOTONS];
Float_t pho_ntrksolidconedr04[MAX_PHOTONS];
Float_t pho_ntrkhollowconedr04[MAX_PHOTONS];
Float_t pho_ecalsumetconedr03[MAX_PHOTONS];
Float_t pho_hcalsumetconedr03[MAX_PHOTONS];
Float_t pho_hcal1sumetconedr03[MAX_PHOTONS];
Float_t pho_hcal2sumetconedr03[MAX_PHOTONS];
Float_t pho_trksumptsolidconedr03[MAX_PHOTONS];
Float_t pho_trksumpthollowconedr03[MAX_PHOTONS];
Float_t pho_ntrksolidconedr03[MAX_PHOTONS];
Float_t pho_ntrkhollowconedr03[MAX_PHOTONS];
Int_t pho_barrel[MAX_PHOTONS];
Int_t pho_scind[MAX_PHOTONS];
Int_t pho_haspixseed[MAX_PHOTONS];
Int_t pho_hasconvtks[MAX_PHOTONS];
Int_t pho_nconv[MAX_PHOTONS];
Int_t pho_isconv[MAX_PHOTONS];
Int_t pho_conv_ntracks[MAX_PHOTONS];
Float_t pho_conv_pairinvmass[MAX_PHOTONS];
Float_t pho_conv_paircotthetasep[MAX_PHOTONS];
Float_t pho_conv_eoverp[MAX_PHOTONS];
Float_t pho_conv_zofprimvtxfromtrks[MAX_PHOTONS];
Float_t pho_conv_distofminapproach[MAX_PHOTONS];
Float_t pho_conv_dphitrksatvtx[MAX_PHOTONS];
Float_t pho_conv_dphitrksatecal[MAX_PHOTONS];
Float_t pho_conv_detatrksatecal[MAX_PHOTONS];
Float_t pho_conv_tk1_d0[MAX_PHOTONS];
Float_t pho_conv_tk1_pout[MAX_PHOTONS];
Float_t pho_conv_tk1_pin[MAX_PHOTONS];
Float_t pho_conv_tk2_d0[MAX_PHOTONS];
Float_t pho_conv_tk2_pout[MAX_PHOTONS];
Float_t pho_conv_tk2_pin[MAX_PHOTONS];
Float_t pho_conv_tk1_dz[MAX_PHOTONS];
Float_t pho_conv_tk1_dzerr[MAX_PHOTONS];
Int_t pho_conv_tk1_nh[MAX_PHOTONS];
Float_t pho_conv_tk2_dz[MAX_PHOTONS];
Float_t pho_conv_tk2_dzerr[MAX_PHOTONS];
Int_t pho_conv_tk2_nh[MAX_PHOTONS];
Int_t pho_conv_ch1ch2[MAX_PHOTONS];
Float_t pho_conv_chi2[MAX_PHOTONS];
Float_t pho_conv_chi2_probability[MAX_PHOTONS];
Int_t pho_conv_validvtx[MAX_PHOTONS];
Float_t pho_conv_MVALikelihood[MAX_PHOTONS];
TClonesArray *pho_p4;
TClonesArray *pho_calopos;
TClonesArray *pho_conv_vtx;
TClonesArray *pho_conv_pair_momentum;
TClonesArray *pho_conv_refitted_momentum;
TClonesArray *pho_conv_vertexcorrected_p4;
Float_t pho_residCorrEnergy[MAX_PHOTONS];
Float_t pho_residCorrResn[MAX_PHOTONS];
Float_t pho_regr_energy[MAX_PHOTONS];
Float_t pho_regr_energyerr[MAX_PHOTONS];

Float_t el_std_regr_energy[MAX_ELECTRONS];
Float_t el_std_regr_energyerr[MAX_ELECTRONS];

Int_t conv_n;
TClonesArray *conv_p4;
Int_t conv_ntracks[MAX_CONVERTEDPHOTONS];
Float_t conv_pairinvmass[MAX_CONVERTEDPHOTONS];
Float_t conv_paircotthetasep[MAX_CONVERTEDPHOTONS];
Float_t conv_eoverp[MAX_CONVERTEDPHOTONS];
Float_t conv_distofminapproach[MAX_CONVERTEDPHOTONS];
Float_t conv_dphitrksatvtx[MAX_CONVERTEDPHOTONS];
Float_t conv_dphitrksatecal[MAX_CONVERTEDPHOTONS];
Float_t conv_detatrksatecal[MAX_CONVERTEDPHOTONS];
Float_t conv_dxy[MAX_CONVERTEDPHOTONS];
Float_t conv_dz[MAX_CONVERTEDPHOTONS];
Float_t conv_lxy[MAX_CONVERTEDPHOTONS];
Float_t conv_lz[MAX_CONVERTEDPHOTONS];
Float_t conv_zofprimvtxfromtrks[MAX_CONVERTEDPHOTONS];
std::vector<std::vector<unsigned short> >* conv_nHitsBeforeVtx;
Int_t conv_nSharedHits[MAX_CONVERTEDPHOTONS];
Int_t conv_validvtx[MAX_CONVERTEDPHOTONS];
Int_t conv_MVALikelihood[MAX_CONVERTEDPHOTONS];
Float_t conv_chi2[MAX_CONVERTEDPHOTONS];
Float_t conv_chi2_probability[MAX_CONVERTEDPHOTONS];
Float_t conv_vtx_xErr[MAX_CONVERTEDPHOTONS];
Float_t conv_vtx_yErr[MAX_CONVERTEDPHOTONS];
Float_t conv_vtx_zErr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_dz[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_dz[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_dzerr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_dzerr[MAX_CONVERTEDPHOTONS];
Int_t conv_tk1_nh[MAX_CONVERTEDPHOTONS];
Int_t conv_tk2_nh[MAX_CONVERTEDPHOTONS];
Int_t conv_ch1ch2[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_d0[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_pout[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_pin[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_d0[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_pout[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_pin[MAX_CONVERTEDPHOTONS];
TClonesArray *conv_vtx;
Float_t conv_tk1_pterr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_pterr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_etaerr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_etaerr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_thetaerr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_thetaerr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_phierr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_phierr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk1_lambdaerr[MAX_CONVERTEDPHOTONS];
Float_t conv_tk2_lambdaerr[MAX_CONVERTEDPHOTONS];
TClonesArray *conv_pair_momentum;
TClonesArray *conv_refitted_momentum;
TClonesArray *conv_singleleg_momentum;
Int_t lptgeninfo_n;
Int_t lptgen_n;
Int_t lptgeninfo_status[MAX_LPT_GENINFO];
Int_t lptgeninfo_pdgid[MAX_LPT_GENINFO];
Int_t lptgeninfo_mother[MAX_LPT_GENINFO];
Int_t  lptgen_status[MAX_LPT_GENINFO];
Int_t lptgen_pdgid[MAX_LPT_GENINFO];
Int_t lptgen_mother[MAX_LPT_GENINFO];
Int_t lptgen_befrad[MAX_LPT_GENINFO];
Int_t lptgen_motherpdgid[MAX_LPT_GENINFO];
Int_t lptgen_indinfo[MAX_LPT_GENINFO];
Int_t lptgen_historycode[MAX_LPT_GENINFO];
Float_t  lptgen_drmatch[MAX_LPT_GENINFO];
Float_t lptgen_drmatchel[MAX_LPT_GENINFO];
Float_t lptgen_drmatchmu[MAX_LPT_GENINFO];
Float_t lptgen_drmatchph[MAX_LPT_GENINFO];
Int_t lptgen_indrec[MAX_LPT_GENINFO];
Int_t lptgen_indrecel[MAX_LPT_GENINFO];
Int_t lptgen_indrecmu[MAX_LPT_GENINFO];
Int_t lptgen_indrecph[MAX_LPT_GENINFO];
TClonesArray *lptgeninfo_p4;
TClonesArray *lptgen_p4;
TClonesArray *lptgen_befrad_p4;
Int_t simtrk_n;
TClonesArray *simtrk_vtx;
TClonesArray *simtrk_p4;
Int_t simtrk_pdgid[MAX_SIMTRACKS];
Int_t simtrk_trkid[MAX_SIMTRACKS];
Int_t simtrk_mothertrkid[MAX_SIMTRACKS];
TClonesArray *simvtx;
std::map<unsigned, unsigned> geantToIndex_;
Int_t simhit_n;
TClonesArray *simhit_xyz;
Float_t simhit_pabs[MAX_SIMHITS];
Float_t simhit_eloss[MAX_SIMHITS];
Int_t simhit_subdet[MAX_SIMHITS];
Int_t simhit_pdgid[MAX_SIMHITS];
Int_t simhit_trkid[MAX_SIMHITS];
Int_t simhit_simtrkind[MAX_SIMHITS];
Int_t tk_n;
Int_t tk_nhits[MAX_TRACKS];
Int_t tk_charge[MAX_TRACKS];
Int_t tk_nlosthit[MAX_TRACKS];
Int_t tk_cmsind[MAX_TRACKS];
Int_t tk_tpind[MAX_TRACKS];
Float_t tk_chi2[MAX_TRACKS];
Float_t tk_dof[MAX_TRACKS];
Float_t tk_d0[MAX_TRACKS];
Float_t tk_dz[MAX_TRACKS];
Float_t tk_qoverperr[MAX_TRACKS];
Float_t tk_pterr[MAX_TRACKS];
Float_t tk_etaerr[MAX_TRACKS];
Float_t tk_phierr[MAX_TRACKS];
Float_t tk_d0err[MAX_TRACKS];
Float_t tk_dzerr[MAX_TRACKS];
Int_t tk_hp_nvalid[MAX_TRACKS];
Int_t tk_hp_nlost[MAX_TRACKS];
Int_t tk_hp_nvalidpix[MAX_TRACKS];
Int_t tk_hp_expin[MAX_TRACKS];
Int_t tk_hp_expout[MAX_TRACKS];
Int_t tk_algo[MAX_TRACKS];
Int_t tk_quality[MAX_TRACKS];
TClonesArray *tk_p4;
TClonesArray *tk_vtx_pos;
Int_t tp_n;
TClonesArray* tp_vtx;
TClonesArray* tp_p4;
TClonesArray* tv_xyz;
Int_t tp_pdgid[MAX_TRACKINGPARTICLES];
Int_t tp_motherid[MAX_TRACKINGPARTICLES];
Int_t tp_charge[MAX_TRACKINGPARTICLES];
Int_t tp_tkind[MAX_TRACKINGPARTICLES];
Int_t tp_genind[MAX_TRACKINGPARTICLES];
Double_t tp_d0[MAX_TRACKINGPARTICLES];
Double_t tp_dz[MAX_TRACKINGPARTICLES];
Int_t vtx_n;
TClonesArray *bs_xyz;
Float_t bs_sigmaZ;
Float_t bs_x0Error;
Float_t bs_y0Error;
Float_t bs_z0Error;
Float_t bs_sigmaZ0Error;
TClonesArray *vtx_xyz;
TClonesArray *vtx_dxdydz;
TClonesArray *vtx_vectorp3;
Float_t vtx_scalarpt[MAX_VERTICES];
Float_t vtx_x2dof[MAX_VERTICES];
Float_t vtx_ndof[MAX_VERTICES];
Int_t vtx_ntks[MAX_VERTICES];
std::vector<std::vector<unsigned short> >* vtx_tkind;
std::vector<std::vector<float> >* vtx_tkweight;
Int_t vtx_std_n;
TClonesArray *bs_std_xyz;
Float_t bs_std_sigmaZ;
Float_t bs_std_x0Error;
Float_t bs_std_y0Error;
Float_t bs_std_z0Error;
Float_t bs_std_sigmaZ0Error;
TClonesArray *vtx_std_xyz;
TClonesArray *vtx_std_dxdydz;
TClonesArray *vtx_std_vectorp3;
Float_t vtx_std_scalarpt[MAX_VERTICES];
Float_t vtx_std_x2dof[MAX_VERTICES];
Float_t vtx_std_ndof[MAX_VERTICES];
Int_t vtx_std_ntks[MAX_VERTICES];
std::vector<std::vector<unsigned short> >* vtx_std_tkind;
std::vector<std::vector<float> >* vtx_std_tkweight;
Float_t pho_r19[MAX_PHOTONS];
Float_t pho_maxoraw[MAX_PHOTONS];
Float_t pho_cep[MAX_PHOTONS];
Float_t pho_lambdaratio[MAX_PHOTONS];
Float_t pho_lambdadivcov[MAX_PHOTONS];
Float_t pho_etawidth[MAX_PHOTONS];
Float_t pho_brem[MAX_PHOTONS];
Float_t pho_smaj[MAX_PHOTONS];
Float_t pho_e2x2[MAX_PHOTONS];
Float_t  pho_pfiso_myneutral01[MAX_PHOTONS];
Float_t  pho_pfiso_myneutral02[MAX_PHOTONS];
Float_t  pho_pfiso_myneutral03[MAX_PHOTONS];
Float_t  pho_pfiso_myneutral04[MAX_PHOTONS];
Float_t  pho_pfiso_myneutral05[MAX_PHOTONS];
Float_t  pho_pfiso_myneutral06[MAX_PHOTONS];
Float_t  pho_pfiso_myphoton01[MAX_PHOTONS];
Float_t  pho_pfiso_myphoton02[MAX_PHOTONS];
Float_t  pho_pfiso_myphoton03[MAX_PHOTONS];
Float_t  pho_pfiso_myphoton04[MAX_PHOTONS];
Float_t  pho_pfiso_myphoton05[MAX_PHOTONS];
Float_t  pho_pfiso_myphoton06[MAX_PHOTONS];
std::vector<std::vector<float> >* pho_pfiso_mycharged01;
std::vector<std::vector<float> >* pho_pfiso_mycharged02;
std::vector<std::vector<float> >* pho_pfiso_mycharged03;
std::vector<std::vector<float> >* pho_pfiso_mycharged04;
std::vector<std::vector<float> >* pho_pfiso_mycharged05;
std::vector<std::vector<float> >* pho_pfiso_mycharged06;
Int_t pho_isPFPhoton[MAX_PHOTONS];
Int_t pho_isPFElectron[MAX_PHOTONS];
Float_t pho_must[MAX_PHOTONS];
Int_t pho_mustnc[MAX_PHOTONS];
Float_t pho_pfpresh1[MAX_PHOTONS];
Float_t pho_pfpresh2[MAX_PHOTONS];
Float_t pho_mustenergy[MAX_PHOTONS];
Float_t pho_mustenergyout[MAX_PHOTONS];
Float_t pho_pflowE[MAX_PHOTONS];
Float_t pho_pfdeta[MAX_PHOTONS];
Float_t pho_pfdphi[MAX_PHOTONS];
Float_t pho_pfclusrms[MAX_PHOTONS];
Float_t pho_pfclusrmsmust[MAX_PHOTONS];
Float_t pho_eseffsixix[MAX_PHOTONS];
Float_t pho_eseffsiyiy[MAX_PHOTONS];
Bool_t jet_algoPF1_pfloose[MAX_JETS];
Bool_t jet_algoPF2_pfloose[MAX_JETS];
Bool_t jet_algoPF3_pfloose[MAX_JETS];
Float_t jet_algoPF3_frac06[MAX_JETS];
Float_t jet_algoPF3_frac07[MAX_JETS];
Float_t jet_algoPF2_frac07[MAX_JETS];
Float_t jet_algoPF2_frac06[MAX_JETS];
Float_t jet_algoPF1_frac06[MAX_JETS];
Float_t jet_algoPF1_frac07[MAX_JETS];
Bool_t jet_algoPF1_genMatched[MAX_JETS];
Bool_t jet_algoPF2_genMatched[MAX_JETS];
Bool_t jet_algoPF3_genMatched[MAX_JETS];
Float_t jet_algoPF3_genPt[MAX_JETS];
Float_t jet_algoPF2_genPt[MAX_JETS];
Float_t jet_algoPF1_genPt[MAX_JETS];
Float_t jet_algoPF1_genDr[MAX_JETS];
Float_t jet_algoPF2_genDr[MAX_JETS];
Float_t jet_algoPF3_genDr[MAX_JETS];
Bool_t jet_algoPF3_vbfMatched[MAX_JETS];
Bool_t jet_algoPF2_vbfMatched[MAX_JETS];
Bool_t jet_algoPF1_vbfMatched[MAX_JETS];
// ELE ID 2012
Float_t  el_std_conv_vtxProb[MAX_ELECTRONS];
Int_t  el_std_conv[MAX_ELECTRONS];
Float_t el_std_pfiso_charged[MAX_ELECTRONS];
Float_t el_std_pfiso_neutral[MAX_ELECTRONS];
Float_t el_std_pfiso_photon[MAX_ELECTRONS];
//
Float_t pho_hcalbcsumetconedr03[MAX_PHOTONS];
Float_t pho_hcalbcsumetconedr04[MAX_PHOTONS];
Float_t pho_hoe_bc[MAX_PHOTONS];
Int_t jet_algoPF1_cutbased_wp_level[MAX_JETS];
Int_t jet_algoPF2_cutbased_wp_level[MAX_JETS];
Int_t jet_algoPF3_cutbased_wp_level[MAX_JETS];
std::vector<std::vector<float>  >* jet_algoPF1_beta_ext;
std::vector<std::vector<float>  >* jet_algoPF1_betaStar_ext;
std::vector<std::vector<float>  >* jet_algoPF1_betaStarClassic_ext;
std::vector<std::vector<float>  >* jet_algoPF2_beta_ext;
std::vector<std::vector<float>  >* jet_algoPF2_betaStar_ext;
std::vector<std::vector<float>  >* jet_algoPF2_betaStarClassic_ext;
std::vector<std::vector<float>  >* jet_algoPF3_beta_ext;
std::vector<std::vector<float>  >* jet_algoPF3_betaStar_ext;
std::vector<std::vector<float>  >* jet_algoPF3_betaStarClassic_ext;
std::vector<std::vector<float> >* pho_pfiso_barecharged01;
std::vector<std::vector<float> >* pho_pfiso_barecharged02;
std::vector<std::vector<float> >* pho_pfiso_barecharged03;
std::vector<std::vector<float> >* pho_pfiso_barecharged04;
std::vector<std::vector<float> >* pho_pfiso_barecharged05;
std::vector<std::vector<float> >* pho_pfiso_barecharged06;
std::vector<std::vector<float> >* pho_pfiso_egcharged01;
std::vector<std::vector<float> >* pho_pfiso_egcharged02;
std::vector<std::vector<float> >* pho_pfiso_egcharged03;
std::vector<std::vector<float> >* pho_pfiso_egcharged04;
std::vector<std::vector<float> >* pho_pfiso_egcharged05;
std::vector<std::vector<float> >* pho_pfiso_egcharged06;
Float_t pho_pfRawEnergy[MAX_PHOTONS];
Float_t pho_pfe2nd[MAX_PHOTONS];
Float_t pho_pfe2x2[MAX_PHOTONS];
Float_t pho_pfe3x3[MAX_PHOTONS];
Float_t pho_pfe5x5[MAX_PHOTONS];
Float_t pho_pfemaxxtal[MAX_PHOTONS];
Float_t pho_pfiso_barephoton01[MAX_PHOTONS];
Float_t pho_pfiso_barephoton02[MAX_PHOTONS];
Float_t pho_pfiso_barephoton03[MAX_PHOTONS];
Float_t pho_pfiso_barephoton04[MAX_PHOTONS];
Float_t pho_pfiso_barephoton05[MAX_PHOTONS];
Float_t pho_pfiso_barephoton06[MAX_PHOTONS];
Float_t pho_pfiso_egphoton01[MAX_PHOTONS];
Float_t pho_pfiso_egphoton02[MAX_PHOTONS];
Float_t pho_pfiso_egphoton03[MAX_PHOTONS];
Float_t pho_pfiso_egphoton04[MAX_PHOTONS];
Float_t pho_pfiso_egphoton05[MAX_PHOTONS];
Float_t pho_pfiso_egphoton06[MAX_PHOTONS];
Float_t pho_pfsieie[MAX_PHOTONS];
Float_t pho_pfsieip[MAX_PHOTONS];
Float_t pho_pfsipip[MAX_PHOTONS];
std::vector<std::vector<int> >* jet_algoPF1_full_wp_level_ext;
std::vector<std::vector<int> >* jet_algoPF1_simple_wp_level_ext;
std::vector<std::vector<int> >* jet_algoPF1_cutbased_wp_level_ext;
std::vector<std::vector<float> >* jet_algoPF1_full_mva_ext;
std::vector<std::vector<float> >* jet_algoPF1_simple_mva_ext;
std::vector<std::vector<int> >* jet_algoPF2_full_wp_level_ext;
std::vector<std::vector<int> >* jet_algoPF2_simple_wp_level_ext;
std::vector<std::vector<int> >* jet_algoPF2_cutbased_wp_level_ext;
std::vector<std::vector<float> >* jet_algoPF2_full_mva_ext;
std::vector<std::vector<float> >* jet_algoPF2_simple_mva_ext;
std::vector<std::vector<int> >* jet_algoPF3_full_wp_level_ext;
std::vector<std::vector<int> >* jet_algoPF3_simple_wp_level_ext;
std::vector<std::vector<int> >* jet_algoPF3_cutbased_wp_level_ext;
std::vector<std::vector<float> >* jet_algoPF3_full_mva_ext;
std::vector<std::vector<float> >* jet_algoPF3_simple_mva_ext;
Float_t jet_algoPF3_area[MAX_JETS];
Float_t jet_algoPF1_area[MAX_JETS];
Float_t jet_algoPF2_area[MAX_JETS];
Float_t jet_algoPF1_nSecondaryVertices[MAX_JETS];
Float_t jet_algoPF1_secVtxPt[MAX_JETS];
Float_t jet_algoPF1_secVtx3dL[MAX_JETS];
Float_t jet_algoPF1_secVtx3deL[MAX_JETS];
Float_t jet_algoPF2_nSecondaryVertices[MAX_JETS];
Float_t jet_algoPF2_secVtxPt[MAX_JETS];
Float_t jet_algoPF2_secVtx3dL[MAX_JETS];
Float_t jet_algoPF2_secVtx3deL[MAX_JETS];
Float_t jet_algoPF3_nSecondaryVertices[MAX_JETS];
Float_t jet_algoPF3_secVtxPt[MAX_JETS];
Float_t jet_algoPF3_secVtx3dL[MAX_JETS];
Float_t jet_algoPF3_secVtx3deL[MAX_JETS];

Float_t jet_algoPF1_ptD_QC[MAX_JETS];
Float_t jet_algoPF1_axis1_QC[MAX_JETS];
Float_t jet_algoPF1_axis2_QC[MAX_JETS];
Int_t jet_algoPF1_nCharged_QC[MAX_JETS];
Int_t jet_algoPF1_nNeutrals_ptCut[MAX_JETS];

Bool_t jet_algoPF1_bgenMatched[MAX_JETS];
Bool_t jet_algoPF2_bgenMatched[MAX_JETS];
Bool_t jet_algoPF3_bgenMatched[MAX_JETS];

