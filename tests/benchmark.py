import numpy as np

def main():
    N = 10_000_000
    print(f"Generatng {N} random numbers...")
    data = np.random.rand(N).astype(np.float32)

    print("\n--- BENCHMARK: gpunum vs numpy ---")
    
    # NumPy
    

    # gpunum

    
        
if __name__ == "__main__":
    main()
