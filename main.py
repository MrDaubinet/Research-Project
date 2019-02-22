from DMGPSO import DMGPSO_AS2
import EvaluationsDynamicLowDimensions
import SetupTruePof
import RunAlgorithm
import DataCollection

def set_true_pof():
    SetupTruePof.SetupTruePof()


def run_algorithm():
    RunAlgorithm.RunAlgorithm(0, 0, 0)
    DataCollection.collect_data("Dynamic POF")


def test_run_algorithm():
    evaluations_dynamic = EvaluationsDynamicLowDimensions.EvaluationsDynamic()
    severity_of_change = [1, 10, 20]
    frequency_of_change = [10, 25, 50]

    for run in range(1):
        evaluations_dynamic.set_severity_of_change(severity_of_change[1])
        evaluations_dynamic.set_frequency_of_change(frequency_of_change[0])
        evaluations_dynamic.set_run(run)
        # evaluations_dynamic.set_dimension_type(0)
        # -- Test fda1 -- #
        evaluations_dynamic.dimp2()
        DMGPSO_AS2.PSODynamic(1000, evaluations_dynamic)

run_algorithm()
# set_true_pof()