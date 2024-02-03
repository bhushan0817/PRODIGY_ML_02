  import matplotlib. pyplot as PI t import seaborn as sns import plotly.express as PX from sklearn . preprocessing import MinMaxSca1er from sklearn . preprocessing import Label Encoder from sklearn . model _ selection import train_test_split from sklearn . metrics import silhouette_ score from sklearn.cluster import KMeans import warnings warnings . filterwarnings ( " ignore" )
In [3] :	 	pd. read_csv(r"C:\Users\susha\ML Jupyter   )
Out[3] :		CustomerID Gender Age Annual Income (k$) Spending Score (1-100)
 
1	Male	19	15	39
2	Male	21	15	81
2	3	Female	20	16	6
3	4	Female	23	16	77
4	5	Female	31	17	40
195	196	Female	35	120	79
196	197	Female	45	126	28
197	198	Male	32	126	74
198	199	Male	32	137	18
199	200	Male	30	137	83
200	rows x 5 columns
In df.info()
<class 'pandas. core. frame.DataFrame'> Rangelndex: 200 entries, e to 199 Data columns (total 5 columns) :
 
	 	Column	Non-Null Count
 
e	CustomerID	200	non-null
1	Gender	200	non-null
2	Age	200	non-null
3	Annual Income (k$)	200	non-null
4	Spending Score (1-100)	200	non-null
dtypes: int64(4), object(l) memory usage: 7.9+ KB
 fig= px.scatter(df, x="Annua1 Income  fig . show()
In	df2	df. drop  "CustomerID" ] )
Dtype
 
int64 object int64 int64 int64
y="Spending Score (1-100)	size="Annua1 ]
