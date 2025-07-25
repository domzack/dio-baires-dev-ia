import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc

y_true = np.random.choice([0, 1, 2], size=1000, p=[0.3, 0.5, 0.2])  # Valores verdadeiros
y_pred = np.random.choice([0, 1, 2], size=1000, p=[0.3, 0.5, 0.2])  # Previsões do modelo

# Gerar matriz de confusão
cm = confusion_matrix(y_true, y_pred)

# Plotar a matriz de confusão
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1, 2], yticklabels=[0, 1, 2])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão (Múltiplas Classes - 10x mais dados)')
plt.show()

# Armazenar métricas para visualização
metricas = {
    "Classe": [],
    "Sensibilidade (Recall)": [],
    "Especificidade": [],
    "Precisão": [],
    "F-Score": []
}

# Calcular métricas para cada classe
classes = [0, 1, 2]
for classe in classes:
    VP = cm[classe, classe]
    FN = np.sum(cm[classe, :]) - VP
    FP = np.sum(cm[:, classe]) - VP
    VN = np.sum(cm) - (VP + FN + FP)
    sensibilidade = VP / (VP + FN) if (VP + FN) > 0 else 0
    especificidade = VN / (VN + FP) if (VN + FP) > 0 else 0
    precisao = VP / (VP + FP) if (VP + FP) > 0 else 0
    fscore = 2 * (precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) > 0 else 0

    # Armazenar métricas
    metricas["Classe"].append(f"Classe {classe}")
    metricas["Sensibilidade (Recall)"].append(sensibilidade)
    metricas["Especificidade"].append(especificidade)
    metricas["Precisão"].append(precisao)
    metricas["F-Score"].append(fscore)

# Plotar gráfico de barras para métricas
plt.figure(figsize=(12, 8))
x = np.arange(len(classes))
width = 0.2

plt.bar(x - width * 1.5, metricas["Sensibilidade (Recall)"], width, label="Sensibilidade (Recall)")
plt.bar(x - width * 0.5, metricas["Especificidade"], width, label="Especificidade")
plt.bar(x + width * 0.5, metricas["Precisão"], width, label="Precisão")
plt.bar(x + width * 1.5, metricas["F-Score"], width, label="F-Score")

plt.xticks(x, metricas["Classe"])
plt.xlabel("Classes")
plt.ylabel("Valores das Métricas")
plt.title("Métricas de Desempenho por Classe")
plt.legend()
plt.show()

# Simulação de probabilidades preditas para cada classe
y_scores = np.random.rand(1000, 3)  # Probabilidades preditas para as classes 0, 1, 2

# Plotar a curva ROC para cada classe
plt.figure(figsize=(10, 8))
for classe in classes:
    y_true_binary = (y_true == classe).astype(int)  # Converter para binário (1 para a classe atual, 0 para as outras)
    fpr, tpr, thresholds = roc_curve(y_true_binary, y_scores[:, classe])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'Classe {classe} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
plt.title('Curva ROC (Múltiplas Classes)')
plt.legend()
plt.show()
