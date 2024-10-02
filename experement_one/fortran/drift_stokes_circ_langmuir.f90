program langmuir_waves_1
  implicit none

  integer, parameter :: Nx = 100, Nz = 20
  real :: u(Nz, Nx), w(Nz, Nx), x(Nx), z(Nz) ! w - вертикальная скорость
  real :: L, H, dx, dz, dt, Tim, t, k, a, omega
  integer :: i, j, nt
  character(len=20) :: filename
  character(len=100) :: filepath
  integer :: unit_num

  ! Параметры системы
  L = 1000.0                  ! Длина области
  H = 200.0                   ! Глубина
  dx = L / Nx                 ! Шаг по x
  dz = H / Nz                 ! Шаг по z
  dt = 0.01                   ! Время шага
  Tim = 100.0                 ! Время моделирования
  k = 2 * 3.14159 / 200.0     ! Волновое число
  a = 1.0                     ! Амплитуда волны
  omega = 2 * 3.14159 / 10.0  ! Угловая частота

  ! Инициализация массива координат
  do i = 1, Nx
    x(i) = (i - 1) * dx
  end do
  do j = 1, Nz
    z(j) = -(j - 1) * dz
  end do

  ! Открытие файла для записи данных
  filename = 'langmuir_data_1.dat'
  ! Формируем полный путь к файлу
  filepath = '.\\data\\output\\' // trim(filename)
  ! Открываем файл
  open(unit=10, file=filepath, status='replace')

  ! Основной цикл моделирования
  do nt = 0, int(Tim / dt)
    t = nt * dt
    ! Вычисление скорости дрифта Стокса
    do i = 1, Nx
      do j = 1, Nz
        u(j, i) = a * k * exp(2 * k * z(j)) * cos(k * x(i) - omega * t)
      end do
    end do

    ! Запись данных в файл каждые 100 шагов
    if (mod(nt, 100) == 0) then
      write(10, '(A, F6.2)') 'Time = ', t
      do j = 1, Nz
        write(10, '(20F10.4)') (u(j, i), i = 1, Nx)
      end do
    end if
  end do

  ! Закрытие файла
  close(10)
end program langmuir_waves_1
