# app.py

from flask import Flask, render_template, jsonify, request, send_file
import tensorflow as tf
import tensorflow_hub as hub
import io

app = Flask(__name__)

# Load the image stylization model
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_img(img_stream):
    img = tf.image.decode_image(img_stream, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

@app.route('/')
def home():
    return render_template('template.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        print('Processing Images...')
        image1 = request.files['image1'].read()
        image2 = request.files['image2'].read()

        # Load the input images
        content_image = load_img(image1)
        style_image = load_img(image2)

        # Stylize the image using the TensorFlow model
        stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

        # Convert the stylized image to bytes
        img_bytes = tf.image.encode_jpeg(tf.cast(stylized_image[0] * 255, tf.uint8)).numpy()
        print("Image processing completed Successfully!")

        # Save the processed image to a temporary file
        temp_filename = 'processed_image.jpg'
        with open(temp_filename, 'wb') as f:
            f.write(img_bytes)

        # Send the processed image file as a response
        return send_file(temp_filename, mimetype='image/jpeg', download_name='processed_image.jpg', as_attachment=True)

    except Exception as e:
        print(str(e))
        return jsonify({'error': 'Image processing failed.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=4949)
