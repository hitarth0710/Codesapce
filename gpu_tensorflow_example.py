"""
Simple GPU Example using TensorFlow
This demonstrates GPU usage with TensorFlow for deep learning
"""

import tensorflow as tf
import time

def check_gpu():
    """Check TensorFlow GPU availability"""
    print("=" * 60)
    print("TensorFlow GPU Check")
    print("=" * 60)
    print(f"TensorFlow version: {tf.__version__}")
    print(f"GPU Available: {tf.config.list_physical_devices('GPU')}")
    print(f"Built with CUDA: {tf.test.is_built_with_cuda()}")
    print()

def simple_gpu_computation():
    """Simple matrix operations on GPU"""
    print("=" * 60)
    print("GPU Matrix Operations")
    print("=" * 60)
    
    # Create large matrices
    size = 3000
    
    with tf.device('/CPU:0'):
        a_cpu = tf.random.normal([size, size])
        b_cpu = tf.random.normal([size, size])
        
        start = time.time()
        c_cpu = tf.matmul(a_cpu, b_cpu)
        cpu_time = time.time() - start
        print(f"CPU time: {cpu_time:.4f} seconds")
    
    if tf.config.list_physical_devices('GPU'):
        with tf.device('/GPU:0'):
            a_gpu = tf.random.normal([size, size])
            b_gpu = tf.random.normal([size, size])
            
            start = time.time()
            c_gpu = tf.matmul(a_gpu, b_gpu)
            gpu_time = time.time() - start
            print(f"GPU time: {gpu_time:.4f} seconds")
            print(f"Speedup: {cpu_time/gpu_time:.2f}x")
    else:
        print("No GPU available for comparison")
    
    print()

def train_simple_model():
    """Train a simple model on GPU"""
    print("=" * 60)
    print("Training Model on GPU")
    print("=" * 60)
    
    # Create a simple model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Generate dummy data
    x_train = tf.random.normal([1000, 784])
    y_train = tf.random.uniform([1000], maxval=10, dtype=tf.int32)
    
    print("Training model...")
    start = time.time()
    history = model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=0)
    training_time = time.time() - start
    
    print(f"Training completed in {training_time:.4f} seconds")
    print(f"Final loss: {history.history['loss'][-1]:.4f}")
    print(f"Final accuracy: {history.history['accuracy'][-1]:.4f}")
    print()

if __name__ == "__main__":
    check_gpu()
    simple_gpu_computation()
    train_simple_model()
