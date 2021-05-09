# arrow_xiao

Seeeduino XIAO���R���g���[���[�Ɏg�p���A
CircuitPython�Ńt�@�[���E�G�A���L�q�����J�[�\���L�[�����̃L�[�{�[�h�ł��B

## �f�[�^

| �t�@�[���E�G�A | main.py        |
| �v���[�g�f�[�^ | arrow_case.pdf |

PCB��su120���g�p���܂����B

## ��H�}

XIAO�̊eGPIO�s���ƃL�[�}�g���b�N�X��row,col�͉��L�̂悤�ɐڑ����܂��B

```
       col0    col1    col2
        = D4    = D5    = D6
             +------+
row0         |      |
 = D2        |  UP  |
             |      |
      +------+------+-------+
row1  |      |      |       |
 = D3 | LEFT | DOWN | RIGHT |
      |      |      |       |
      +------+------+-------+
```

## �t�@�[���E�G�A

�����̃h�L�������g(https://wiki.seeedstudio.com/jp/Seeeduino-XIAO-CircuitPython/)���Q�l��
CircuitPython�̃u�[�g���[�_�[��XIAO�ɃC���X�g�[�����Ă��������B

HID�f�o�C�X�Ƃ��Ďg�p���邽�߂Ƀ��C�u�����[��CircuitPython�̃T�C�g(https://circuitpython.org/libraries)����_�E�����[�h����,
adafruit_hid�t�H���_����XIAO��lib�t�H���_�փR�s�[���Ă��������B

���̃��|�W�g����main.py��XIAO�ɃR�s�[���Ă��������B

## ����ɂ���

�ǂꂩ�L�[�������Ă���Ԃ�XIAO�̉��F��LED���_�����܂��B

�R�̃L�[�𓯎����������ꍇ��20�b���ƂɃJ�[�\���������I�ɏ㉺�A����A���E�A�E���ɓ��삵�܂��A�ǂꂩ�L�[�����������Ă���Ύ~�܂�܂��B
