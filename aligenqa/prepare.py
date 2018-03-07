import ROOT
import settings

from rootpy.io import root_open
import re, os

from aligenqa import utils
from aligenqa.plotting import Plotting
from aligenqa import roofie

def prepare(args):
    """
    This will download AnalysisResults.root from the given alien path ...
    """
    args.local_path = download(args)
    plot(args)

def download(args):
    ROOT.gROOT.SetBatch(True)
    gen_name = utils.get_generator_name_from_train(args.input_file)
    train_number = re.match(r'.*/(\d+_\d{8}-\d{4})', args.input_file).groups()[-1]
    _, fext = os.path.splitext(os.path.basename(args.input_file))
    local_path = os.path.abspath(os.path.join("./", "{0}-{1}{2}".format(train_number, gen_name, fext)))
    utils.download_file(args.input_file, local_path)
    return local_path

def plot(args):
    ROOT.gROOT.SetBatch(True)

    for global_trigger in settings.considered_triggers:
        sums_dir_name = "Sums" + global_trigger
        results_dir_name = "results_post" + global_trigger

        plotting = Plotting(f_name=args.local_path, sums_dir_name=sums_dir_name, results_dir_name=results_dir_name,
                            percentile_bins=settings.percentile_bins, considered_ests=settings.considered_ests)

        # call Plotting's memberfunctions to create the desired plots:
        plotting.plot_dNdetas(ratio_to_mb=False)
        plotting.plot_dNdetas(ratio_to_mb=True)
        plotting.plot_PNch_summary()
        plotting.plot_PNch()
        plotting.plot_mult_vs_pt()
        plotting.plot_meanpt_vs_ref_mult_for_pids()
        plotting.plot_pt_distribution_ratios()
        plotting.plot_pid_ratio_vs_refmult()
        plotting.plot_dNdpT(pid_selection='ch')
        plotting.plot_dNdpT(pid_selection='p')
        plotting.plot_dNdpT(pid_selection='pi')
        plotting.plot_dNdpT(pid_selection='K')
        plotting.plot_pT_HM_div_pt_MB(scale_nMPI=False)
        plotting.plot_pT_HM_div_pt_MB(scale_nMPI=True)
        plotting.plot_nMPI_vs_Nch()
