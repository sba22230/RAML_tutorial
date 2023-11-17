import TASSC_20058_stable as btr
import TAASSC_215_dev as lgr

import glob
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Directory location of your text files.')
    parser.add_argument('--directory', type=str, help="Directory of your text files.")
    parser.add_argument('--filename', type=str, help="Name of the .csv file with your results.")
    parser.add_argument('--dev', type=bool, help="Set to True if you want to use the version current in development",
                        default=False)
    args = parser.parse_args()

    file_list = glob.glob("%s/*.txt" % args.directory)  # create your own filelist

    if not args.dev:

        btr.BTR_XML(file_list, "%s.csv" % args.filename)
        btr.BTR_XML(args.directory, "%s.csv" % args.filename)  # let TAASSC generate the filelist based on a folder name
        btr.BTR_XML("%s/" % args.directory, "%s.csv" % args.filename,
                     output=["xml"])  # generate summary count file, generate xml representation for each
        btr.BTR_XML("%s/" % args.directory, "%s.csv" % args.filename, output=["xml",
                                                                "vertical"])  # generate summary count file, generate xml representation  and vertical representation for each

    else:
        lgr.LGR_Full(file_list, "%s.csv" % args.filename)
        lgr.LGR_Full(args.directory,
                  "%s.csv" % args.filename)  # let TAASSC generate the filelist based on a folder name
        lgr.LGR_Full("%s/" % args.directory, "%s.csv" % args.filename,
                  output=["xml"])  # generate summary count file, generate xml representation for each
        lgr.LGR_Full("%s/" % args.directory, "%s.csv" % args.filename, output=["xml",
                                                                               "vertical"])  # generate summary count file, generate xml representation  and vertical representation for each



