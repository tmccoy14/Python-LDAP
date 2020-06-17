"""Standard library"""
import re

"""Third party modules"""
import ldap
from ldap import filter as ldap_filter


# LDAP settings
LDAP_SERVER = "ldap://server"
BASE_DN = "dc=example,dc=com"
LDAP_LOGIN = "EXAMPLE\Admin"
LDAP_PASSWORD = "password"

# Active Directory search filters
USER = ""
OBJECT_TO_SEARCH = "(&(objectclass=person)(CN=%s))"
ATTRIBUTES_TO_SEARCH = ["memberOf"]


def ldap_connection():
    """Open connection with LDAP server."""

    # Open a connection with the LDAP server
    connect = ldap.initialize(LDAP_SERVER)

    # Tell LDAP server not to chase referrals
    connect.set_option(ldap.OPT_REFERRALS, 0)

    # bind server with credentials
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)

    # Return LDAP connection
    return connect


def ldap_search(ldap_connect, user):
    """Search LDAP server for groups a user is a member of."""

    records = ldap_connect.search_s(
        BASE_DN,
        ldap.SCOPE_SUBTREE,
        ldap_filter.filter_format(OBJECT_TO_SEARCH, (user,)),
        ATTRIBUTES_TO_SEARCH,
    )

    ldap_connect.unbind_s()

    if "memberOf" in records[0][1]:
        groups = records[0][1]["memberOf"]
        result = [re.findall(b"(?:cn=|CN=)(.*?),", group)[0] for group in groups]
        result = [r.decode("utf-8") for r in result]
        print(result)


if __name__ == "__main__":
    """Set up LDAP server connection and execute search"""

    ldap_connect = ldap_connection()
    ldap_search(ldap_connect, USER)
