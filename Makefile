RPM_WORKING     = $(PWD)

RPM_ARGS          = --nodeps
RPM_ARGS         += --nodigest
RPM_ARGS         += --nosignature
RPM_ARGS         += --clean
RPM_ARGS         += --buildroot $(RPM_WORKING)/BROOT

RPM_BUILD         = -bb

TARGET_CPU        = i686
TARGET_VENDOR     = RHEL
TARGET_OS         = linux
RPM_TARGET        = $(TARGET_CPU)-$(TARGET_VENDOR)-$(TARGET_OS)

RPM_INSTALL_ARG   = -iv
RPM_INSTALL_ARG  += --nosignature
RPM_INSTALL_ARG  += --nodigest
RPM_INSTALL_ARG  += --nodeps
RPM_INSTALL_ARG  += --nomd5

SPECS             = Leap

all:
	mkdir -p $(RPM_WORKING)/{BUILD,RPMS,SOURCES,SPECS,SRPMS,BROOT}
	$(foreach spec, $(SPECS), rpmbuild $(RPM_BUILD) $(RPM_ARGS) SPECS/$(spec).spec;)
	$(foreach spec, $(SPECS), rm -rf $(RPM_WORKING)/RPMS/$(TARGET_CPU)/$(spec)-debuginfo*.rpm;)

clean:
	rm -rf $(RPM_WORKING)/BROOT $(RPM_WORKING)/BUILD $(RPM_WORKING)/RPMS $(RPM_WORKING)/SRPMS
