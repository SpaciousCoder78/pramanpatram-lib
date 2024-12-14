import os
from pramanpatram.pramanpatram import Pramanpatram

def test_generate_certificate():
    csv_path = "attendees.csv"
    sample_path = "sample.jpg"
    text_coords_x = 450
    text_coords_y = 530
    text_size = 20
    r_value = 0
    g_value = 0
    b_value = 0
    text_width = 40
    certificate_text = "Thanks {name}"
    certificate_path = "certificates"

    if not os.path.exists(csv_path):
        print(f"CSV file not found at path: {csv_path}")
        return

    if not os.path.exists(certificate_path):
        os.makedirs(certificate_path)
        print(f"Created directory for certificates at path: {certificate_path}")

    patram = Pramanpatram()
    result = patram.generate_certificates(csv_path, sample_path, text_coords_x, text_coords_y, text_size, r_value, g_value, b_value, text_width, certificate_text, certificate_path)
    print(result)

test_generate_certificate()