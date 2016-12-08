import sys,os,pkgutil


def load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name
                        ).load_module(full_package_name)
            print module



def main():
    load_all_modules_from_dir('E1')
    load_all_modules_from_dir('E2')
    load_all_modules_from_dir('E3')
    load_all_modules_from_dir('E4')
    load_all_modules_from_dir('E5')
    load_all_modules_from_dir('E6')
    load_all_modules_from_dir('E7')
    print "Archivo principal"

if __name__ == '__main__':
        main()
