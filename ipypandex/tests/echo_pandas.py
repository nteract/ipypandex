import pandas as pd
from IPython.utils.capture import capture_output
with capture_output() as c:
    display(pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}))
print(c.outputs[0].data)
