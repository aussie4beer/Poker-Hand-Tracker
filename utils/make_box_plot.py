import matplotlib.pyplot as plt


def make_box_plot(save_to_folder: str, x_axis_labels, data, x_label, y_label, title, size=(10, 10), range_=range(1, 46)):
    plt.figure(figsize=size)
    plt.yticks(range_)
    plt.grid(alpha=0.3)
    plt.boxplot(data, labels=x_axis_labels)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # plt.show()
    figure_name = str(title + '.jpg').replace(' ', '_')
    plt.savefig(save_to_folder + figure_name, dpi=300, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, pad_inches=1, metadata=None)
    return figure_name
