"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    os.makedirs('files/plots', exist_ok=True)

    dataset = pd.read_csv('files/input/news.csv', sep=',', index_col=0)

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey'
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2
    }

    fig, ax = plt.subplots()

    for column in dataset.columns:
        ax.plot(
            dataset[column],
            label=column,
            color=colors[column],
            zorder=zorder[column],
            linewidth=linewidths[column],
        )

    ax.set_title('How people get their news', fontsize=16)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_yaxis().set_visible(False)

    for column in dataset.columns:
        first_year = dataset.index[0]
        ax.scatter(
            x=first_year,
            y=dataset[column][first_year],
            color=colors[column]
        )

        ax.text(
            first_year - 0.25,
            dataset[column][first_year],
            column + " " + str(dataset[column][first_year]) + '%',
            ha='right',
            va='center',
            color=colors[column]

        )

        last_year = dataset.index[-1]
        ax.scatter(
            x=last_year,
            y=dataset[column][last_year],
            color=colors[column]
        )

        ax.text(
        last_year + 0.25,
        dataset[column][last_year],
        str(dataset[column][last_year]) + '%',
        ha='left',
        va='center',
        color=colors[column]
        )

    ax.set_xticks(
        ticks=dataset.index,
        labels=dataset.index,
        ha='center'
    )

    plt.tight_layout()
    plt.savefig('files/plots/news.png')
    plt.show()

pregunta_01()