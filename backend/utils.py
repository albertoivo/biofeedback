import base64
from io import BytesIO


def matplotlib_to_base64(plt):
    """
    Transform a Matplotlib graph to a base 64 url.

    :param plt: The matplotlib graph after plotting it.
    :return: the matplotlib graph in base64.
    """
    try:
        figfile = BytesIO()
        plt.savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())
        result = 'data:image/png;base64,{}'.format(figdata_png.decode("utf-8"))
    finally:
        plt.cla()
        plt.clf()
        plt.close()

    return result
