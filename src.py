"""Third party modules"""
import ldap


def ldap_connection():
    """open connection with LDAP server"""

    # disabling certificate check for testing purposes
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    # open a connection with the LDAP server
    connect = ldap.initialize("ldaps://server")

    # tell server not to chase referrals
    connect.set_option(ldap.OPT_REFERRALS, 0)

    # bind server with credentials
    connect.simple_bind_s("user", "password")

    # return ldap connection
    return connect


def ldap_search(ldap_connect):
    """search LDAP server"""
    result = ldap_connect.search_s(
        "dc=somedomain,dc=com",
        ldap.SCOPE_SUBTREE,
        "userPrincipalName=user@somedomain.com",
        ["memberOf"],
    )


if __name__ == "__main__":
    """set up LDAP server connection and execute search"""

    ldap_connect = ldap_connection()
    ldap_search(ldap_connect)
