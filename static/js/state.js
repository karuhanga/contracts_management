var app_state;
var contracts = [];
var companies = [];
var managers = [];
var notifs = [];
var app;
var CORE_URL = "http://127.0.0.1:8000/";
const ADD = "add";
const UPDATE = "update";
const COMPANIES = "Companies";
const CONTRACTS = "Contracts";
const MANAGERS = "Managers";
const NOTIFICATION = "Notifications";
const COMPANIES_URL = CORE_URL + "companies";
const CONTRACTS_URL = CORE_URL + "contracts";
const MANAGERS_URL = CORE_URL + "managers";
const NOTIFICATIONS_URL = CORE_URL + "notifications";
const separator = "/";
var DEBUG = false;
var loaded;

function log(message) {
    // if (DEBUG) {
    //     console.log(message);
    // }
    console.log(message);
}

function matches(constraint) {
    return function (element) {
        return !(element.name.search(constraint) === -1);
    }
}

function fetch_fake_data() {

    contracts = [
        {
            pk: "id",
            name: "Contract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        },
        {
            pk: "id",
            name: "ontract",
            section: "Department",
            company: "Contractor",
            start_date: "Started",
            expiry_date: "Expires",
            popup_active: false
        }
    ];

    companies = [
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        },
        {
            pk: "id",
            name: "ame",
            contact_person: "contact_person",
            email: "email",
            contact: "contact",
            popup_active: false
        }
    ];

    managers = [
        {pk: "id", name: "adme", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "xsme", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "fgme", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "ame", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "Name", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "Name", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "Name", email: "email", contact: "contact", popup_active: false},
        {pk: "id", name: "Name", email: "email", contact: "contact", popup_active: false}
    ];

    notifs = [
        {name: "name", when_time_left: "when_time_left"},
        {name: "name", when_time_left: "when_time_left"},
        {name: "name", when_time_left: "when_time_left"},
        {name: "name", when_time_left: "when_time_left"},
        {name: "name", when_time_left: "when_time_left"},
        {name: "name", when_time_left: "when_time_left"}
    ];

    app.contracts = contracts;
    app.companies = companies;
    app.managers = managers;
    app.notifs = notifs;
}

function fetch_contracts() {
    fetch(CONTRACTS_URL).then(function (data) {
        data.json().then(function (value) {
            contracts = value;
            app.contracts = value;
        })
    });
}

function fetch_companies() {
    fetch(COMPANIES_URL).then(function (data) {
        data.json().then(function (value) {
            companies = value;
            app.companies = value;
        })
    });
}

function fetch_managers() {
    fetch(MANAGERS_URL).then(function (data) {
        data.json().then(function (value) {
            managers = value;
            app.managers = value;
        })
    });
}

function fetch_notifs() {
    fetch(NOTIFICATIONS_URL).then(function (data) {
        data.json().then(function (value) {
            notifs = value;
            app.notifs = value;
        })
    });
}

function fetch_data() {
    if (DEBUG) {
        fetch_fake_data();
        initApp();
        return;
    }

    fetch_contracts();

    fetch_companies();

    fetch_managers();

    fetch_notifs();
}

function toast_ok(message) {
    nativeToast({
        message: message,
        position: 'bottom',
        timeout: 3000,
        type: 'success',
        square: true
    });
}

function toast_err(message) {
    nativeToast({
        message: message,
        position: 'bottom',
        timeout: 3000,
        type: 'error',
        square: true
    });
}

function refreshData(current) {
    switch (current) {
        case CONTRACTS:
            fetch_contracts();
            break;
        case "Companies":
            fetch_companies();
            break;
        case "Managers":
            fetch_managers();
            break;
        case "Notifications":
            fetch_notifs();
            break;
        default:
            fetch_data();
    }
}

function initVariables() {
    app_state = {
        el: '#app',
        data: {
            current: CONTRACTS,
            current_singular: "Contract",
            current_state: false,
            upcoming_active: true,
            all_active: false,
            notifs_active: false,
            searching: false,
            contracts: contracts,
            companies: companies,
            managers: managers,
            notifs: notifs,
            search_text: "",
            sort_menu_active: false,
            companies_active: false,
            managers_active: false,
            add_active: false,
            delete_active: false,
            add_source: "",
            loading: false,
            action: "Add",
            in_delete: ""
        },
        methods: {
            details: function (pk) {
                this.action = "Detailed";
                this.loading = true;
                this.add_active = true;
                switch (this.current_singular) {
                    case "Company":
                        this.add_source = COMPANIES_URL + separator + pk;
                        break;
                    case "Contract":
                        this.add_source = CONTRACTS_URL + separator + pk;
                        break;
                }
            },
            cancel_delete: function () {
                this.in_delete = "";
                this.delete_active = false;
            },
            confirm_delete: function () {
                var entity = "";
                this.delete_active = false;
                switch (this.current) {
                    case "Companies":
                        entity = "companies";
                        break;
                    case CONTRACTS:
                        entity = "contracts";
                        break;
                    case "Managers":
                        entity = "managers";
                        break;
                    case "Notifications":
                        entity = "notifications";
                        break;
                }
                var cs = this.current_singular;
                fetch(CORE_URL + entity + separator + this.in_delete + "/delete").then(function (value) {
                    log(value);
                    if (value.ok) {
                        toast_ok("Deleted " + cs);
                        refreshData(cs);
                    }
                    else {
                        toast_err("Failed to delete " + cs + " (Still referenced elsewhere)");
                    }
                }).catch(function (reason) {
                    log(reason);
                    toast_err("Failed to delete " + cs);
                });
            },
            content_holder_loaded: function () {
                this.loading = false;
            },
            close_add: function () {
                refreshData("__all__");
                this.add_active = false;
                this.add_source = "";
            },
            add_clicked: function () {
                this.action = "Add";
                this.loading = true;
                this.add_active = true;
                switch (this.current_singular) {
                    case "Company":
                        this.add_source = COMPANIES_URL + separator + ADD;
                        break;
                    case "Contract":
                        this.add_source = CONTRACTS_URL + separator + ADD;
                        break;
                    case "Manager":
                        this.add_source = MANAGERS_URL + separator + ADD;
                        break;
                    case "Notification":
                        this.add_source = NOTIFICATIONS_URL + separator + ADD;
                        break;
                }
            },
            edit_clicked: function (pk) {
                this.action = "Edit";
                this.loading = true;
                this.add_active = true;
                switch (this.current_singular) {
                    case "Company":
                        this.add_source = COMPANIES_URL + separator + pk + separator + UPDATE;
                        break;
                    case "Contract":
                        this.add_source = CONTRACTS_URL + separator + pk + separator + UPDATE;
                        break;
                    case "Manager":
                        this.add_source = MANAGERS_URL + separator + pk + separator + UPDATE;
                        break;
                }
            },
            delete_clicked: function (pk) {
                this.in_delete = pk;
                this.delete_active = true;
            },
            sort_upcoming: function () {
                // TODO
                this.sort_menu_active = false;
            },
            sort_section: function () {
                // TODO
                this.sort_menu_active = false;
            },
            clear_all: function () {
                var contract;
                this.sort_menu_active = false;
                for (contract in contracts) {
                    contracts[contract]['popup_active'] = false;
                }
            },
            clear_all_company: function () {
                var company;
                for (company in companies) {
                    companies[company]['popup_active'] = false;
                }
            },
            clear_all_manager: function () {
                var manager;
                for (manager in managers) {
                    managers[manager]['popup_active'] = false;
                }
            },
            toggle: function () {
                this.searching = !this.searching;
            },
            show_companies: function () {
                log("clicked");
                this.companies_active = true;
                this.managers_active = false;
                this.upcoming_active = false;
                this.all_active = false;
                this.notifs_active = false;
                this.add_active = false;
                this.current = "Companies";
                this.current_singular = "Company";
            },
            show_managers: function () {
                this.managers_active = true;
                this.upcoming_active = false;
                this.all_active = false;
                this.notifs_active = false;
                this.companies_active = false;
                this.add_active = false;
                this.current = "Managers";
                this.current_singular = "Manager";
            },
            show_upcoming: function () {
                this.upcoming_active = true;
                this.all_active = false;
                this.notifs_active = false;
                this.companies_active = false;
                this.managers_active = false;
                this.add_active = false;
                this.sort_upcoming();
                this.current = CONTRACTS;
                this.current_singular = "Contract";
            },
            show_all: function () {
                this.all_active = true;
                this.upcoming_active = false;
                this.notifs_active = false;
                this.companies_active = false;
                this.managers_active = false;
                this.add_active = false;
                this.current = CONTRACTS;
                this.current_singular = "Contract";
            },
            show_notifs: function () {
                this.notifs_active = true;
                this.upcoming_active = false;
                this.all_active = false;
                this.companies_active = false;
                this.add_active = false;
                this.notifs = notifs;
                this.managers_active = false;
                this.current = "Notifications";
                this.current_singular = "Notification";
            },
            contract_details: function () {
                // TODO
            },
            company_details: function () {
                // TODO
            }
        },
        watch: {
            // upcoming_active : function () {
            //     this.all_active = false;
            // },
            // all_active : function () {
            //     this.upcoming_active = false;
            // },
            search_text: function () {
                var v_instance;
                var instance;
                switch (this.current) {
                    case CONTRACTS:
                        this.contracts = contracts.filter(matches(this.search_text));
                        break;
                    case "Companies":
                        this.companies = companies.filter(matches(this.search_text));
                        break;
                    case "Managers":
                        this.managers = managers.filter(matches(this.search_text));
                        break;
                    // default: this.contracts = contracts.filter(matches(this.search_text)); break;
                }
            },
            searching: function () {
                if (!this.searching) {
                    this.search_text = "";
                }
            }
        },
        computed: {
            not_searching: function () {
                return !this.searching;
            }
        }
    };
}

function initApp() {
    log("initApp");
    initVariables();
    buildApp();
    fetch_data();
}


function buildApp() {
    log("built app!");
    app = new Vue(app_state);
}

window.addEventListener('load', function () {
    log("loaded!");
    initApp();
});