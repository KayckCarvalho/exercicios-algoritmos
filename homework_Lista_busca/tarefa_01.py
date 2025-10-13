import random
import time
import sys
import tracemalloc
from typing import List, Tuple, Optional

class ComparadorBusca:
    def __init__(self, tamanho: int = 1000000):
        self.tamanho = tamanho
        self.lista = self._gerar_lista()
        
    def _gerar_lista(self) -> List[int]:
        """Gera uma lista de números inteiros aleatórios ordenada"""
        print(f"Gerando lista com {self.tamanho} elementos...")
        lista = [random.randint(1, self.tamanho * 10) for _ in range(self.tamanho)]
        lista.sort()
        return lista
    
    def busca_sequencial(self, alvo: int) -> Tuple[Optional[int], int]:
        """
        Implementa busca sequencial
        Retorna: (índice, número de comparações)
        """
        comparacoes = 0
        for indice, elemento in enumerate(self.lista):
            comparacoes += 1
            if elemento == alvo:
                return indice, comparacoes
            if elemento > alvo:
                break
        return None, comparacoes
    
    def busca_binaria(self, alvo: int) -> Tuple[Optional[int], int]:
        """
        Implementa busca binária iterativa
        Retorna: (índice, número de comparações)
        """
        comparacoes = 0
        inicio, fim = 0, len(self.lista) - 1
        
        while inicio <= fim:
            comparacoes += 1
            meio = (inicio + fim) // 2
            
            if self.lista[meio] == alvo:
                return meio, comparacoes
            elif self.lista[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
                
        return None, comparacoes
    
    def medir_tempo_memoria(self, funcao_busca, alvo: int, nome: str):
        """Mede tempo de execução e uso de memória para uma função de busca"""
        print(f"\n--- {nome} ---")
        
        tracemalloc.start()
        
        inicio_tempo = time.time()
        resultado, comparacoes = funcao_busca(alvo)
        fim_tempo = time.time()
        
        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        tempo_execucao = (fim_tempo - inicio_tempo) * 1000  
        
        print(f"Alvo: {alvo}")
        print(f"Resultado: {resultado}")
        print(f"Comparações realizadas: {comparacoes}")
        print(f"Tempo de execução: {tempo_execucao:.6f} ms")
        print(f"Memória atual: {memoria_atual / 1024:.2f} KB")
        print(f"Memória de pico: {memoria_pico / 1024:.2f} KB")
        
        return tempo_execucao, comparacoes, memoria_pico
    
    def executar_testes(self):
        """Executa testes comparativos para diferentes cenários"""
        print("=" * 60)
        print(f"COMPARADOR DE ALGORITMOS DE BUSCA")
        print(f"Lista com {self.tamanho} elementos")
        print("=" * 60)
        
        cenarios = [
            ("Melhor caso (primeiro elemento)", self.lista[0]),
            ("Caso médio (elemento do meio)", self.lista[self.tamanho // 2]),
            ("Pior caso (último elemento)", self.lista[-1]),
            ("Elemento não existente", -1)
        ]
        
        resultados = []
        
        for nome_cenario, alvo in cenarios:
            print(f"\n{'='*50}")
            print(f"CENÁRIO: {nome_cenario}")
            print(f"{'='*50}")
            
            tempo_seq, comp_seq, mem_seq = self.medir_tempo_memoria(
                self.busca_sequencial, alvo, "BUSCA SEQUENCIAL"
            )
            
            tempo_bin, comp_bin, mem_bin = self.medir_tempo_memoria(
                self.busca_binaria, alvo, "BUSCA BINÁRIA"
            )
            
            resultados.append({
                'cenario': nome_cenario,
                'sequencial': {'tempo': tempo_seq, 'comparacoes': comp_seq, 'memoria': mem_seq},
                'binaria': {'tempo': tempo_bin, 'comparacoes': comp_bin, 'memoria': mem_bin}
            })
        
        self._apresentar_resultados_comparativos(resultados)
    
    def _apresentar_resultados_comparativos(self, resultados):
        """Apresenta resultados comparativos finais"""
        print("\n" + "="*70)
        print("RESULTADOS COMPARATIVOS FINAIS")
        print("="*70)
        
        for resultado in resultados:
            print(f"\n{resultado['cenario']}:")
            seq = resultado['sequencial']
            bin = resultado['binaria']
            
            if seq['tempo'] > 0 and bin['tempo'] > 0:
                razao_tempo = seq['tempo'] / bin['tempo']
                print(f"  Velocidade: Busca Binária é {razao_tempo:.1f}x mais rápida")
            
            razao_comp = seq['comparacoes'] / bin['comparacoes']
            print(f"  Comparações: Sequencial={seq['comparacoes']}, Binária={bin['comparacoes']} ({razao_comp:.1f}x menos)")
            
            razao_mem = seq['memoria'] / bin['memoria']
            print(f"  Memória: Similar (Razão: {razao_mem:.2f}x)")

def analise_complexidade():
    """Análise teórica da complexidade dos algoritmos"""
    print("\n" + "="*70)
    print("ANÁLISE TEÓRICA DE COMPLEXIDADE")
    print("="*70)
    
    analise = {
        'Busca Sequencial': {
            'Melhor Caso': 'O(1) - elemento na primeira posição',
            'Caso Médio': 'O(n/2) ≈ O(n)',
            'Pior Caso': 'O(n) - elemento na última posição ou não existe',
            'Memória': 'O(1) - espaço constante'
        },
        'Busca Binária': {
            'Melhor Caso': 'O(1) - elemento no meio',
            'Caso Médio': 'O(log n)',
            'Pior Caso': 'O(log n)',
            'Memória': 'O(1) - versão iterativa'
        }
    }
    
    for algoritmo, complexidades in analise.items():
        print(f"\n{algoritmo}:")
        for caso, descricao in complexidades.items():
            print(f"  {caso}: {descricao}")

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    
    comparador = ComparadorBusca(1000000) 
    comparador.executar_testes()
    
    analise_complexidade()
    
    print("\n" + "="*70)
    print("TESTE ESTATÍSTICO 100 BUSCAS ALEATÓRIAS")
    print("="*70)
    
    tempos_seq = []
    tempos_bin = []
    
    for _ in range(100):
        alvo_aleatorio = random.choice(comparador.lista)
        
        inicio = time.time()
        comparador.busca_sequencial(alvo_aleatorio)
        tempos_seq.append((time.time() - inicio) * 1000)
        
        inicio = time.time()
        comparador.busca_binaria(alvo_aleatorio)
        tempos_bin.append((time.time() - inicio) * 1000)
    
    print(f"Busca Sequencial - Média: {sum(tempos_seq)/len(tempos_seq):.6f} ms")
    print(f"Busca Binária - Média: {sum(tempos_bin)/len(tempos_bin):.6f} ms")