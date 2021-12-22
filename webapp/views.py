import asyncio

from django.http import HttpResponse
from django.views import View

from .common import measure, multitask

r_c = 0


async def action(t, ref):
    await measure(asyncio.sleep(t), ref)


async def actions(n, t, ref):
    func = lambda i: action(t, f'{ref} | Task {i}')
    await measure(multitask(func, n), ref)


async def async_view(request, *args, **kwargs):
    global r_c
    r_c += 1
    await actions(2, 3, f'View {r_c}')
    return HttpResponse('Ok')


class AsyncCbv(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, *args, **kwargs):
        global r_c
        r_c += 1
        await actions(2, 3, f'CBV {r_c}')
        return HttpResponse('Ok')
