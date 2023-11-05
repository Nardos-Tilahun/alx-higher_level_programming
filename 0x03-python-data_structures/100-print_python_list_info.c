#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - print python list
 * @p: pyobject
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
