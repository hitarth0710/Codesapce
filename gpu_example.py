"""
GPU Computing Example for Codespace
This script demonstrates various GPU operations using PyTorch
"""

import torch
import time
import numpy as np

def check_gpu_availability():
    """Check and display GPU information"""
    print("=" * 60)
    print("GPU AVAILABILITY CHECK")
    print("=" * 60)
    
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"Number of GPUs: {torch.cuda.device_count()}")
        print(f"Current GPU: {torch.cuda.current_device()}")
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    else:
        print("CUDA not available. Using CPU instead.")
    
    print()

def matrix_multiplication_benchmark():
    """Compare CPU vs GPU performance for matrix multiplication"""
    print("=" * 60)
    print("MATRIX MULTIPLICATION BENCHMARK")
    print("=" * 60)
    
    size = 5000
    
    # CPU computation
    print(f"Creating {size}x{size} matrices on CPU...")
    cpu_a = torch.randn(size, size)
    cpu_b = torch.randn(size, size)
    
    start = time.time()
    cpu_result = torch.matmul(cpu_a, cpu_b)
    cpu_time = time.time() - start
    print(f"CPU computation time: {cpu_time:.4f} seconds")
    
    # GPU computation (if available)
    if torch.cuda.is_available():
        print(f"\nCreating {size}x{size} matrices on GPU...")
        gpu_a = torch.randn(size, size, device='cuda')
        gpu_b = torch.randn(size, size, device='cuda')
        
        # Warm up GPU
        _ = torch.matmul(gpu_a, gpu_b)
        torch.cuda.synchronize()
        
        start = time.time()
        gpu_result = torch.matmul(gpu_a, gpu_b)
        torch.cuda.synchronize()
        gpu_time = time.time() - start
        
        print(f"GPU computation time: {gpu_time:.4f} seconds")
        print(f"Speedup: {cpu_time/gpu_time:.2f}x faster on GPU")
    
    print()

def neural_network_training():
    """Simple neural network training on GPU"""
    print("=" * 60)
    print("NEURAL NETWORK TRAINING ON GPU")
    print("=" * 60)
    
    # Set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}\n")
    
    # Create a simple neural network
    class SimpleNN(torch.nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc1 = torch.nn.Linear(784, 256)
            self.fc2 = torch.nn.Linear(256, 128)
            self.fc3 = torch.nn.Linear(128, 10)
            self.relu = torch.nn.ReLU()
            
        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.fc3(x)
            return x
    
    # Initialize model and move to GPU
    model = SimpleNN().to(device)
    print(f"Model created with {sum(p.numel() for p in model.parameters())} parameters")
    
    # Create dummy data
    batch_size = 128
    X = torch.randn(batch_size, 784, device=device)
    y = torch.randint(0, 10, (batch_size,), device=device)
    
    # Training setup
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    # Training loop
    print("\nTraining for 100 iterations...")
    start = time.time()
    
    for i in range(100):
        # Forward pass
        outputs = model(X)
        loss = criterion(outputs, y)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i + 1) % 20 == 0:
            print(f"Iteration {i+1}/100, Loss: {loss.item():.4f}")
    
    training_time = time.time() - start
    print(f"\nTraining completed in {training_time:.4f} seconds")
    
    if torch.cuda.is_available():
        print(f"GPU Memory allocated: {torch.cuda.memory_allocated(0) / 1e9:.4f} GB")
        print(f"GPU Memory reserved: {torch.cuda.memory_reserved(0) / 1e9:.4f} GB")
    
    print()

def image_processing_example():
    """GPU-accelerated image processing"""
    print("=" * 60)
    print("IMAGE PROCESSING ON GPU")
    print("=" * 60)
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}\n")
    
    # Create a batch of random images (batch, channels, height, width)
    batch_size = 32
    images = torch.randn(batch_size, 3, 224, 224, device=device)
    
    print(f"Processing batch of {batch_size} images (224x224x3)...")
    
    # Apply various transformations
    start = time.time()
    
    # Normalize
    normalized = (images - images.mean()) / images.std()
    
    # Apply a simple convolution (edge detection)
    conv_filter = torch.tensor([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ], dtype=torch.float32, device=device).view(1, 1, 3, 3)
    
    # Apply filter to each channel
    edges = torch.nn.functional.conv2d(
        normalized, 
        conv_filter.repeat(3, 1, 1, 1),
        groups=3,
        padding=1
    )
    
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    
    processing_time = time.time() - start
    print(f"Processing completed in {processing_time:.4f} seconds")
    print(f"Output shape: {edges.shape}")
    print()

def main():
    """Run all GPU examples"""
    print("\n" + "=" * 60)
    print("GPU COMPUTING EXAMPLES")
    print("=" * 60 + "\n")
    
    # Check GPU availability
    check_gpu_availability()
    
    # Run benchmarks
    matrix_multiplication_benchmark()
    
    # Neural network training
    neural_network_training()
    
    # Image processing
    image_processing_example()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
