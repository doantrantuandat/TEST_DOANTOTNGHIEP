#-----------------------------------------------------------------------
# File    : sam.mak
# Contents: build sam program (split and merge) (on Windows systems)
# Author  : Christian Borgelt
# History : 2008.10.15 file created from relim makefile
#           2010.02.12 module pfxtree replaced by module clomax
#           2010.08.22 module escape added (for module tabread)
#           2011.08.29 external module fim16 added (16 items machine)
#           2016.04.20 completed dependencies on header files
#-----------------------------------------------------------------------
THISDIR  = ..\..\sam\src
UTILDIR  = ..\..\util\src
TRACTDIR = ..\..\tract\src

CC       = cl.exe
DEFS     = /D WIN32 /D NDEBUG /D _CONSOLE /D _CRT_SECURE_NO_WARNINGS
CFLAGS   = /nologo /W3 /O2 /GS- $(DEFS) /c $(ADDFLAGS)
INCS     = /I $(UTILDIR) /I $(TRACTDIR)

LD       = link.exe
LDFLAGS  = /nologo /subsystem:console /incremental:no
LIBS     = 

HDRS     = $(UTILDIR)\fntypes.h    $(UTILDIR)\arrays.h     \
           $(UTILDIR)\memsys.h     $(UTILDIR)\symtab.h     \
           $(UTILDIR)\tabread.h    $(UTILDIR)\tabwrite.h   \
           $(UTILDIR)\error.h      $(TRACTDIR)\tract.h     \
           $(TRACTDIR)\patspec.h   $(TRACTDIR)\clomax.h    \
           $(TRACTDIR)\report.h    $(TRACTDIR)\fim16.h
OBJS     = $(UTILDIR)\arrays.obj   $(UTILDIR)\memsys.obj   \
           $(UTILDIR)\idmap.obj    $(UTILDIR)\escape.obj   \
           $(UTILDIR)\tabread.obj  $(UTILDIR)\tabwrite.obj \
           $(UTILDIR)\scform.obj   $(TRACTDIR)\taread.obj  \
           $(TRACTDIR)\patspec.obj $(TRACTDIR)\clomax.obj  \
           $(TRACTDIR)\repcm.obj   $(TRACTDIR)\fim16.obj sam.obj
PRGS     = sam.exe

#-----------------------------------------------------------------------
# Build Program
#-----------------------------------------------------------------------
all:       $(PRGS)

sam.exe:   $(OBJS) sam.mak
	$(LD) $(LDFLAGS) $(OBJS) $(LIBS) /out:$@

#-----------------------------------------------------------------------
# Main Programs
#-----------------------------------------------------------------------
sam.obj:   $(HDRS) sam.mak
	$(CC) $(CFLAGS) $(INCS) /D SAM_MAIN sam.c /Fo$@

#-----------------------------------------------------------------------
# External Modules
#-----------------------------------------------------------------------
$(UTILDIR)\arrays.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak arrays.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\memsys.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak memsys.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\idmap.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak idmap.obj    ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\escape.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak escape.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\tabread.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak tabread.obj  ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\tabwrite.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak tabwrite.obj ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\scform.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak scform.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(TRACTDIR)\taread.obj:
	cd $(TRACTDIR)
	$(MAKE) /f tract.mak taread.obj  ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(TRACTDIR)\patspec.obj:
	cd $(TRACTDIR)
	$(MAKE) /f tract.mak patspec.obj ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(TRACTDIR)\clomax.obj:
	cd $(TRACTDIR)
	$(MAKE) /f tract.mak clomax.obj  ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(TRACTDIR)\repcm.obj:
	cd $(TRACTDIR)
	$(MAKE) /f tract.mak repcm.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(TRACTDIR)\fim16.obj:
	cd $(TRACTDIR)
	$(MAKE) /f tract.mak fim16.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)

#-----------------------------------------------------------------------
# Install
#-----------------------------------------------------------------------
install:
	-@copy $(PRGS) ..\..\..\bin

#-----------------------------------------------------------------------
# Clean up
#-----------------------------------------------------------------------
localclean:
	-@erase /Q *~ *.obj *.idb *.pch $(PRGS)

clean:
	$(MAKE) /f sam.mak localclean
	cd $(TRACTDIR)
	$(MAKE) /f tract.mak localclean
	cd $(UTILDIR)
	$(MAKE) /f util.mak clean
	cd $(THISDIR)
