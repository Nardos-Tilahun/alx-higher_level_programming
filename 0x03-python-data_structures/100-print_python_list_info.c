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

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li\n", list->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
