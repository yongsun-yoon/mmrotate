import mmcv
import mmengine
import mmdet
from mmengine.utils import digit_version

__version__ = '1.0.0rc1'
short_version = __version__

mmcv_version = digit_version(mmcv.__version__)
mmengine_version = digit_version(mmengine.__version__)
mmdet_version = digit_version(mmdet.__version__)

__all__ = ['__version__', 'short_version', 'digit_version']
