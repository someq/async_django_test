from django.test import TestCase
from django.urls import reverse

from .common import measure, multitask


class AsyncTest(TestCase):
    async def get(self, url, ref):
        coro = self.async_client.get(url)
        await measure(coro, ref)

    async def test_async_view(self):
        url = reverse('webapp:async_view')
        func = lambda i: self.get(url, f'Test View {i}')
        await measure(multitask(func, 5), 'Test View')

    async def test_async_cbv(self):
        url = reverse('webapp:async_cbv')
        func = lambda i: self.get(url, f'Test CBV {i}')
        await measure(multitask(func, 5), 'Test CBV')

    async def test_mixed(self):
        view_url = reverse('webapp:async_view')
        cbv_url = reverse('webapp:async_cbv')
        func = lambda i: self.get(
            view_url if i % 2 == 0 else cbv_url,
            f'Test | Mixed {i}'
        )
        await measure(multitask(func, 10), 'Test Mixed')
