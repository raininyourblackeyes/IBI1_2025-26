import matplotlib.pyplot as plt
import numpy as np

#create a dictionary
genes = {'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3, 'ESP1':10.7}
print(genes)
#add gene 'MYC'
genes['MYC'] = 11.6
print(genes)

#create a bar chart
genes_names = list(genes.keys())
expression_values = list(genes.values())

plt.bar(genes_names, expression_values)
plt.title("Gene expression")

plt.xlabel('Gene Name')
plt.ylabel('Expression Value')
plt.tight_layout()
plt.show()

#create a variable
gene_of_interest = input("What's your interested gene?")
if gene_of_interest in genes_names:
    print(f"\n{gene_of_interest}'s gene expression：{genes[gene_of_interest]}")
else:
    print(f"\nThe gene is wrong: gene{gene_of_interest}is not in the dataset!")

#calculate the average of gene expression
avg_expression = sum(genes.values()) / len(expression_values)
print(f"The average of gene expression is{avg_expression}.")
