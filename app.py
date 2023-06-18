from flask import Flask, request, jsonify, send_from_directory
import os
import datetime
import uuid
import json

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # Generate UID for the uploaded file
        uid = str(uuid.uuid4())

        # Extract original filename
        filename = file.filename

        # Generate new filename with timestamp and UID
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        new_filename = f"{filename}_{timestamp}_{uid}"

        # Save the file in the uploads folder
        file.save(os.path.join('uploads', new_filename))

        # Return the JSON object with the UID
        return jsonify({'uid': uid})
    else:
        return jsonify({'error': 'No file uploaded'}), 400

@app.route('/status/<uid>', methods=['GET'])
def check_status(uid):
    # Check if the file exists in the uploads folder
    uploads_dir = 'uploads'
    matching_files = [filename for filename in os.listdir(uploads_dir) if uid in filename]
    if len(matching_files) == 0:
        # No upload found with the given UID
        return jsonify({'status': 'not found'}), 404
    else:
        # Extract details from the filename
        filename = matching_files[0].split('_')[0]
        timestamp = matching_files[0].split('_')[1]

        # Check if the output file exists
        output_file = f"output/{uid}.json"
        if os.path.exists(output_file):
            # Upload has been processed
            with open(output_file, 'r') as f:
                explanation = json.load(f)
            return jsonify({'status': 'done', 'filename': filename, 'timestamp': timestamp, 'explanation': explanation})
        else:
            # Upload is still pending
            return jsonify({'status': 'pending', 'filename': filename, 'timestamp': timestamp})


@app.route('/uploads/<filename>', methods=['GET'])
def serve_upload(filename):
    return send_from_directory('uploads', filename)
