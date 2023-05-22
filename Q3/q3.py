import pandas as pd
import numpy as np

def sort_store():
    a = np.array([[1000, 280, 900], [25, 120, 30]])

    df = pd.DataFrame(a.T, index=['store1', 'store2', 'store3'], columns=['unit price', 'number'])

    print(df)
    print("\n")
    df['total price'] = df['unit price'] * df['number']
    df2 = df.sort_values(by='total price', ascending=False)

    print(df)
    print("\n")
    print(df2.head(2))

if __name__ == "__main__":
    sort_store()
