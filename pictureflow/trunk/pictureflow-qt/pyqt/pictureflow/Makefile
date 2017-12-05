TARGET = pictureflow.so
OFILES = sippictureflowcmodule.o sippictureflowPictureFlow.o
HFILES = sipAPIpictureflow.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DQT_NO_DEBUG -DQT_CORE_LIB -DQT_GUI_LIB -I. -I/media/geunho/UUI/Project17-2/pictureflow/trunk/pictureflow-qt -I/usr/include/python2.7 -I/usr/share/qt4/mkspecs/default -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtGui -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS =  -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security  -D_FORTIFY_SOURCE=2 -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS =  -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security  -D_FORTIFY_SOURCE=2 -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS =  -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-O1 -shared  -Wl,-O1 -Wl,--version-script=pictureflow.exp
LIBS = -L/media/geunho/UUI/Project17-2/pictureflow/trunk/pictureflow-qt/pyqt -L/media/geunho/UUI/Project17-2/pictureflow/trunk/pictureflow-qt/pyqt/lib -L/usr/lib -L/usr/X11R6/lib -lpictureflow -lQtCore -lQtGui
MOC = moc-qt4
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	@echo '{ global: initpictureflow; local: *; };' > pictureflow.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/$(TARGET)

clean:
	-rm -f $(TARGET)
	-rm -f sippictureflowcmodule.o
	-rm -f sippictureflowPictureFlow.o
	-rm -f pictureflow.exp
