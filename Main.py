from __future__ import division
import PSO
import PSODynamic
import Evaluations
import EvaluationsDynamic

def main():
    evaluations_dynamic = EvaluationsDynamic.EvaluationsDynamic()
    severity_of_change = [1, 10, 20]
    frequency_of_change = [10, 25, 50]

    # -- Test DIMP2 -- #
    evaluations_dynamic.dimp2()
    for run in range(1):
        evaluations_dynamic.set_severity_of_change(severity_of_change[0])
        evaluations_dynamic.set_frequency_of_change(frequency_of_change[0])
        evaluations_dynamic.set_run(run)
        PSODynamic.PSODynamic(2000, evaluations_dynamic)

main()