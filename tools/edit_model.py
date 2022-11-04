import torch
# 保留enhance
# pre_model='basepre_SOTA.pth'
# dict = torch.load(pre_model)
# for key in list(dict.keys()):
#     if not key.startswith('enhance'):
#         del dict[key]
# torch.save(dict, './basepre_enhance.pth')
# 保留detector
# pre_model='basepre_SOTA.pth'
# dict = torch.load(pre_model)
# for key in list(dict.keys()):
#     if key.startswith('enhance'):
#         del dict[key]
# torch.save(dict, './basepre_det.pth')

pre_model='basepre_SOTA.pth'
dict = torch.load(pre_model)
for key in list(dict.keys()):
    if not key.startswith('enhance'):
        del dict[key]
for key in list(dict.keys()):
    tmp=key.split('.')[1:]
    tmp='.'.join(tmp)
    dict[tmp]=dict[key]
torch.save(dict, './ceshi.pth')