# Python Naming Conventions

## PEP 8 -- Styleguide for Python Code
See [PEP 8 -- Styleguide for Python Code](https://www.python.org/dev/peps/pep-0008/) for in-depth information.

---


| Typ | Public | Private / Internal |
|-----|--------|--------------------|
| Packages | ```lower_with_under``` ||
| Modules | ```lower_with_under``` | ```_lower_with_under``` |
| Classes | ```CapWords``` | ```_CapWords``` |
| Exceptions | ```CapWords``` ||
| Functions | ```lower_with_under()``` | ```_lower_with_under()``` |
| Global Class Constants | ```CAPS_WITH_UNDER``` | ```_CAPS_WITH_UNDER``` |
| Global Class Variables | ```lower_with_under``` | ```_lower_with_under``` |
| Instance Variables | ```lower_with_under``` | ```_lower_with_under``` |
| Method Names | ```lower_with_under()``` | ```_lower_with_under()``` |
| Function / Method Parameters | ```lower_with_under``` ||
| Local Variables | ```lower_with_under``` ||