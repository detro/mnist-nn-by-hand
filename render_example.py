import random
import argparse

from dataset_loaders import mnist
from render import terminal

def select_data_set(data: str, set: str):
    match data, set:
        case "mnist", "training":
            return mnist.load_training()
        case "mnist", "testing":
            return mnist.load_testing()
        # TODO support EMNIST
        case _:
            raise ValueError(
                f"Invalid combination of data set ({data}) and set ({set})."
            )

def select_id(arg_id: int, data_size: int):
    if arg_id is None:
        return random.randrange(0, data_size)
    return arg_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = "Render example image from a dataset."
    parser.add_argument("--data", type=str, default="mnist", choices=["mnist"])
    parser.add_argument("--set", type=str, default="training", choices=["training", "testing"])
    parser.add_argument("--id", type=int, default=None)
    args = parser.parse_args()

    imgs, lbls = select_data_set(args.data, args.set)
    id = select_id(args.id, len(imgs))

    print(f"* Data Set: {args.data} ({args.set}) (size: {len(imgs)})")
    print(f"* Image ID: {id}")
    print(f"* Image Label: {lbls[id]}")
    terminal.print_img(imgs[id])
