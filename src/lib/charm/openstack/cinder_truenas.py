import charms_openstack.charm
import charmhelpers.core.hookenv as ch_hookenv  # noqa

charms_openstack.charm.use_defaults('charm.default-select-release')


class CinderTrueNASCharm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_truenas'
    version_package = 'cinder-driver-truenas'
    release = 'ocata'
    packages = [version_package]
    release_pkg = version_package
    stateless = True
    # Specify any config that the user *must* set.
    mandatory_config = [
        'ixsystems-api-key',
        'ixsystems-server-hostname',
        'ixsystems-iqn-prefix',
        'ixsystems-datastore-pool',
        'ixsystems-dataset-path'
    ]

    def cinder_configuration(self):
        volume_driver = 'cinder.volume.drivers.ixsystems.iscsi.FreeNASISCSIDriver'
        driver_options = [
            ('volume_driver', volume_driver),
            ('ixsystems_api_key', self.config.get('ixsystems-api-key')),
            ('ixsystems_server_hostname', self.config.get('ixsystems-server-hostname')),
            ('ixsystems_volume_backend_name', self.config.get('ixsystems-volume-backend-name')),
            ('ixsystems_iqn_prefix', self.config.get('ixsystems-iqn-prefix')),
            ('ixsystems_datastore_pool', self.config.get('ixsystems-datastore-pool')),
            ('ixsystems_dataset_path', self.config.get('ixsystems-dataset-path')),
            ('ixsystems_vendor_name', self.config.get('ixsystems-vendor-name')),
            ('ixsystems_storage_protocol', self.config.get('ixsystems-storage-protocol'))
        ]
        return driver_options


class CinderTrueNASCharmRocky(CinderTrueNASCharm):

    # Rocky needs py3 packages.
    release = 'rocky'
    version_package = 'cinder-driver-truenas'
    packages = [version_package]
