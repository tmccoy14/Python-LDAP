"""Third party modules"""
import ldap

# LDAP settings
LDAP_SERVER = "ldap://server"
BASE_DN = "dc=example,dc=com"
LDAP_LOGIN = "AFSDIGITAL\Admin"
LDAP_PASSWORD = "password"

# Active Directory search filters
OBJECT_TO_SEARCH = "(&(objectclass=person)(CN=User))"
ATTRIBUTES_TO_SEARCH = ["memberOf"]


def ldap_connection():
    """open connection with LDAP server"""

    # Open a connection with the LDAP server
    connect = ldap.initialize(LDAP_SERVER)

    # Tell LDAP server not to chase referrals
    connect.set_option(ldap.OPT_REFERRALS, 0)

    # bind server with credentials
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)

    # Return LDAP connection
    return connect


def ldap_search(ldap_connect):
    """search LDAP server"""

    # Search Active Directory
    result = ldap_connect.search_s(
        BASE_DN, ldap.SCOPE_SUBTREE, OBJECT_TO_SEARCH, ATTRIBUTES_TO_SEARCH
    )

    # Print search results
    print(result)


if __name__ == "__main__":
    """Set up LDAP server connection and execute search"""

    ldap_connect = ldap_connection()
    ldap_search(ldap_connect)
