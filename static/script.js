async function processImages() {
    const image1 = document.getElementById('image1').files[0];
    const image2 = document.getElementById('image2').files[0];

    if (!image1 || !image2) {
        alert('Please select both images.');
        return;
    }

    const formData = new FormData();
    formData.append('image1', image1);
    formData.append('image2', image2);

    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Image processing failed.');
        }

        const contentType = response.headers.get('content-type');

        if (contentType && contentType.includes('application/json')) {
            try {
                const clonedResponse = response.clone();
                const result = await clonedResponse.json();
                const processedImage = document.getElementById('processedImage');
                processedImage.src = result.output_url;
                processedImage.addEventListener('load', function () {
                    console.log('Image Loaded Successfully!');
                });
            } catch (error) {
                console.error('Error parsing JSON:', error);
                alert('Image processing failed. Please try again.');
            }
        } else {
            const blob = await response.blob();
            const processedImage = document.getElementById('processedImage');
            processedImage.src = URL.createObjectURL(blob);
            processedImage.addEventListener('load', function () {
                console.log('Image Loaded Successfully!');
            });
        }
    } catch (error) {
        console.error(error);
        alert('Image processing failed. Please try again.');
    }
}
