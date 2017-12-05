import pandas
dataset = pandas.read_csv('pcap_indusoft_PC.csv')

y, X = train['Classification'], train[['DGMLEN', 'IPLEN', 'IP']].fillna(0)
X_Modeltrain, X_Modeltest, y_Modeltrain, y_Modeltest = train_Modeltest_split(X, y, test_size=0.1, random_state=29)
lr = LogisticRegression()
lr.fit(X_Modeltrain, y_Modeltrain)
print (accuracy_score(y_Modeltest, lr.predict(X_Modeltest)))