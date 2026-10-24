from torch.utils.tensorboard import SummaryWriter

training = [0.8, 0.5, 0.3, 0.1]
validation = [0.9, 0.7, 0.8, 1.0]

with SummaryWriter("runs/loss_demo") as writer:
    for epoch, (train_loss, val_loss) in enumerate(zip(training, validation), start=1):
        writer.add_scalar("loss/train", train_loss, epoch)
        writer.add_scalar("loss/validation", val_loss, epoch)