/****************************************************************************
** Meta object code from reading C++ file 'pictureflow.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../pictureflow.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'pictureflow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_PictureFlow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       4,   79, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      19,   13,   12,   12, 0x05,

 // slots: signature, parameters, type, tag, flags
      49,   43,   12,   12, 0x0a,
      73,   66,   12,   12, 0x0a,
     103,   91,   12,   12, 0x0a,
     137,  124,   12,   12, 0x0a,
     159,   13,   12,   12, 0x0a,
     179,   12,   12,   12, 0x0a,
     187,   12,   12,   12, 0x0a,
     202,   12,   12,   12, 0x0a,
     213,   13,   12,   12, 0x0a,
     228,   12,   12,   12, 0x0a,
     237,   12,   12,   12, 0x0a,
     253,   12,   12,   12, 0x08,

 // properties: name, type, flags
     278,  271, 0x43095103,
     300,  294, 0x15095103,
     314,  310, 0x02095001,
     325,  310, 0x02095103,

       0        // eod
};

static const char qt_meta_stringdata_PictureFlow[] = {
    "PictureFlow\0\0index\0centerIndexChanged(int)\0"
    "image\0addSlide(QImage)\0pixmap\0"
    "addSlide(QPixmap)\0index,image\0"
    "setSlide(int,QImage)\0index,pixmap\0"
    "setSlide(int,QPixmap)\0setCenterIndex(int)\0"
    "clear()\0showPrevious()\0showNext()\0"
    "showSlide(int)\0render()\0triggerRender()\0"
    "updateAnimation()\0QColor\0backgroundColor\0"
    "QSize\0slideSize\0int\0slideCount\0"
    "centerIndex\0"
};

void PictureFlow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        PictureFlow *_t = static_cast<PictureFlow *>(_o);
        switch (_id) {
        case 0: _t->centerIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->addSlide((*reinterpret_cast< const QImage(*)>(_a[1]))); break;
        case 2: _t->addSlide((*reinterpret_cast< const QPixmap(*)>(_a[1]))); break;
        case 3: _t->setSlide((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< const QImage(*)>(_a[2]))); break;
        case 4: _t->setSlide((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< const QPixmap(*)>(_a[2]))); break;
        case 5: _t->setCenterIndex((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->clear(); break;
        case 7: _t->showPrevious(); break;
        case 8: _t->showNext(); break;
        case 9: _t->showSlide((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 10: _t->render(); break;
        case 11: _t->triggerRender(); break;
        case 12: _t->updateAnimation(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PictureFlow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PictureFlow::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_PictureFlow,
      qt_meta_data_PictureFlow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PictureFlow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PictureFlow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PictureFlow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PictureFlow))
        return static_cast<void*>(const_cast< PictureFlow*>(this));
    return QWidget::qt_metacast(_clname);
}

int PictureFlow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< QColor*>(_v) = backgroundColor(); break;
        case 1: *reinterpret_cast< QSize*>(_v) = slideSize(); break;
        case 2: *reinterpret_cast< int*>(_v) = slideCount(); break;
        case 3: *reinterpret_cast< int*>(_v) = centerIndex(); break;
        }
        _id -= 4;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setBackgroundColor(*reinterpret_cast< QColor*>(_v)); break;
        case 1: setSlideSize(*reinterpret_cast< QSize*>(_v)); break;
        case 3: setCenterIndex(*reinterpret_cast< int*>(_v)); break;
        }
        _id -= 4;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 4;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 4;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 4;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 4;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 4;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 4;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void PictureFlow::centerIndexChanged(int _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE
