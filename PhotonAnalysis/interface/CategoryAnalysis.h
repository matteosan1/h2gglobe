#ifndef __CATEGORYANALYSIS__
#define __CATEGORYANALYSIS__

#include "BaseAnalysis.h"
#include "BaseSmearer.h"
#include "PhotonAnalysis.h"
#include "StatAnalysis.h"
#include "RooContainer.h"
#include "VertexAnalysis/interface/HggVertexAnalyzer.h"

#include "EnergySmearer.h"
#include "EfficiencySmearer.h"
#include "DiPhoEfficiencySmearer.h"
#include "KFactorSmearer.h"
#include <iostream>
#include <fstream>
#include "math.h"

// ------------------------------------------------------------------------------------
class CategoryAnalysis : public StatAnalysis 
{
 public:
    
    CategoryAnalysis();
    virtual ~CategoryAnalysis();
    
    virtual const std::string & name() const { return name_; };
    
    // LoopAll analysis interface implementation
    void Init(LoopAll&);
    void Term(LoopAll&);
    
    virtual void ResetAnalysis();
    //// virtual void Analysis(LoopAll&, Int_t); 

    virtual int GetBDTBoundaryCategory(float,bool,bool);

    bool doPhotonMvaIdSyst;
    bool doPhotonMvaIdSmear;
    bool doRegressionSmear, doRegressionSyst;
    bool doPdfWeightSmear, doPdfWeightSyst;

    std::string bdtTrainingPhilosophy;
    std::string bdtTrainingType;
    std::string photonLevelMvaUCSD  ;
    std::string eventLevelMvaUCSD   ;                    
    std::string photonLevel2011IDMVA_EB;
    std::string photonLevel2011IDMVA_EE;
    std::string eventLevelMvaMIT    ;
    std::string photonLevel2012IDMVA_EB;
    std::string photonLevel2012IDMVA_EE;

    std::vector<float> bdtCategoryBoundaries;

 protected:

    virtual bool AnalyseEvent(LoopAll& l, Int_t jentry, float weight, TLorentzVector & gP4, float & mass, float & evweight, int & category, int & diphoton_id,
		      bool & isCorrectVertex, float &kinematic_bdtout,
		      bool isSyst=false, 
		      float syst_shift=0., bool skipSelection=false,
		      BaseGenLevelSmearer *genSys=0, BaseSmearer *phoSys=0, BaseDiPhotonSmearer * diPhoSys=0); 

    EnergySmearer  *eRegressionSmearer ; 
    DiPhoEfficiencySmearer *photonMvaIdSmearer ;
    
    std::string name_;
    std::map<int,std::string> signalLabels;
    
};

#endif


// Local Variables:
// mode: c++
// mode: sensitive
// c-basic-offset: 4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
