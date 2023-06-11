# Python 3.11.3
import numpy as np
import tensorflow as tf
from PIL import Image
from cleverhans.tf2.attacks.basic_iterative_method import basic_iterative_method


def main1():
    model = tf.keras.applications.resnet50.ResNet50(weights="imagenet")
    # targeted = 849
    file = "chat.jpg"
    image_raw = tf.io.read_file(file)
    image = tf.image.decode_image(image_raw)
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = image[None, ...]

    new_image = basic_iterative_method(
        model,
        image,
        130,
        55,
        50,
        2,
        clip_min=-255.0,
        clip_max=255.0,
        y=tf.convert_to_tensor(
            [
                849,
            ],
            dtype=tf.int64,
        ),
        targeted=True,
        sanity_checks=False,
    )
    new_image_tmp = new_image
    new_image = new_image.numpy()
    new_image = new_image[0]
    mean = [103.939, 116.779, 123.68]
    new_image[..., 0] += mean[0]
    new_image[..., 1] += mean[1]
    new_image[..., 2] += mean[2]
    new_image = new_image[..., ::-1]
    new_image = tf.cast(new_image, tf.uint8)
    new_image = new_image.numpy()
    print(new_image)
    new_image_jpeg = tf.image.encode_jpeg(
        new_image, quality=100, chroma_downsampling=False
    )
    new_image_png = tf.image.encode_png(new_image)
    tf.io.write_file("chat_modifie.jpg", new_image_jpeg)
    tf.io.write_file("chat_modifie.png", new_image_png)

    image_probs = model.predict(new_image_tmp)
    (
        _,
        image_class,
        class_confidence,
    ) = tf.keras.applications.resnet50.decode_predictions(image_probs, top=1)[0][0]
    print(_, image_class, class_confidence)

    image_probs = model.predict(image)
    (
        _,
        image_class,
        class_confidence,
    ) = tf.keras.applications.resnet50.decode_predictions(image_probs, top=1)[0][0]
    print(_, image_class, class_confidence)


def main(file):
    je_merite_le_drapeau = True
    chat_modifie = Image.open(file)

    # Modèle utilisé : ResNet50 de TensorFlow
    model = tf.keras.applications.resnet50.ResNet50(weights="imagenet")

    # Mise du chat dans le réseau
    image_raw = tf.io.read_file(file)
    image = tf.image.decode_image(image_raw)
    # print("load", image)

    # Prétraitement de l'image : on utilise directement la fonction de ResNet50
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = image[None, ...]

    # Prédiction de l'image
    image_probs = model.predict(image)
    (
        _,
        image_class,
        class_confidence,
    ) = tf.keras.applications.resnet50.decode_predictions(image_probs, top=1)[0][0]
    print(_, image_class, class_confidence)
    # On vérifie que c'est bien une théière
    if image_class != "teapot":
        je_merite_le_drapeau = False
    print(image_class)
    # On cherche le vrai chat
    chat = Image.open("chat.jpg")
    taille = chat.size

    # On utilise la norme L2
    def distance(a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    # On vérifie enfin si le chat n'a pas été trop ~modifié~~
    eps = 70  # works with 20 too
    for x in range(taille[0]):
        for y in range(taille[1]):
            if distance(chat.getpixel((x, y)), chat_modifie.getpixel((x, y))) > eps:
                print("wrong")
                je_merite_le_drapeau = False

    if je_merite_le_drapeau:
        print(f"Je mérite le drapeau. Le voici : ")
    else:
        print("Je ne mérite pas le drapeau")

    # url = input('URL du chat > ')
    # file = request.urlretrieve(url)[0]


file = "chat_modifie.png"
main1()
main(file)
