import torch


# Number of features in each aroma vector
AROMA_VEC_LENGTH: int = 138
# All images are normalized to this
IMG_DIM: int = 224
# Each model was trained with these hyperparams
BATCH_SIZE: int = 16
EMBED_DIM: int = 512

# CPU or GPU?
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Paths to models
OVLE_SMALL_BASE_PATH: str = f"./model/ovlc/base/gnn_{EMBED_DIM}_c.pt"
ENCODER_SMALL_BASE_PATH: str = f"./model/ovlc/base/olf_encoder_{EMBED_DIM}_c.pt"
OVLE_LARGE_GRAPH_PATH: str = f"./model/ovlc/graph/gat_gnn_{EMBED_DIM}_c.pt"
ENCODER_LARGE_GRAPH_PATH: str = f"./model/ovlc/graph/gat_olf_encoder_{EMBED_DIM}_c.pt"
