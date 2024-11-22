import matplotlib.pyplot as plt
from utilities import FileReader




def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file()
    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append(val[-1] - first_stamp)

    
    
    fig, axes = plt.subplots(2,1, figsize=(14,6))

    plt.subplots_adjust(hspace=0.4)

    ##### plotting for point with extra odom varaibles #####
    # axes[0].plot([lin[len(headers) - 5] for lin in values], [lin[len(headers) - 4] for lin in values])
    
    axes[0].plot([lin[len(headers) - 3] for lin in values], [lin[len(headers) - 2] for lin in values])
    axes[0].set_title("State Space")
    axes[0].set_xlabel("State Variable X (m)")
    axes[0].set_ylabel("State Variable Y (m)")
    axes[0].grid()
    
    axes[1].set_title("Each Individual State")
    axes[1].set_xlabel("Time (ns)")
    axes[1].set_ylabel("State Variable Magnitudes")
    for i in range(0, len(headers) - 1):
        axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i])

    axes[1].legend(bbox_to_anchor=(1.12, 0), loc='lower right')
    axes[1].grid()

    plt.show()
    
    





import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename)


